import logging
from typing import (
    Any,
    List,
    Dict,
    Type,
    Generic,
    TypeVar
)

from mongoengine.base import BaseDocument
from mongoengine.queryset.base import BaseQuerySet

import pydantic
from pydantic import BaseModel

from google.protobuf.message import Message
from google.protobuf.json_format import MessageToDict, ParseDict

from grpc_pydantic_mongoengine.proto.base import base_pb2

from .utils import update_document

logger = logging.getLogger(__name__)

# Mongo Engine Model types
ModelType = TypeVar("ModelType", bound=BaseDocument)

# Protobuf Model Types
CreateProtobufMessageType = TypeVar("CreateProtobufMessageType", bound=Message)
UpdateProtobufMessageType = TypeVar("UpdateProtobufMessageType", bound=Message)
SingleDataProtobufMessageType = TypeVar("SingleDataProtobufMessageType", bound=Message)
MultiDataProtobufMessageType = TypeVar("MultiDataProtobufMessageType", bound=Message)

# Pydantic Schema Types
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
DataSchemaType = TypeVar("DataSchemaType", bound=BaseModel)


class CRUDBaseGrpc(
    Generic[
        ModelType,
        CreateProtobufMessageType,
        UpdateProtobufMessageType,
        SingleDataProtobufMessageType,
        MultiDataProtobufMessageType,
        CreateSchemaType,
        UpdateSchemaType,
        DataSchemaType
    ]
):
    def __init__(
            self,
            model: Type[ModelType],
            create_protobuf_message_class: Type[CreateProtobufMessageType],
            update_protobuf_message_class: Type[UpdateProtobufMessageType],
            single_protobuf_message_class: Type[SingleDataProtobufMessageType],
            multi_protobuf_message_class: Type[MultiDataProtobufMessageType],
            create_schema_class: Type[CreateSchemaType],
            update_schema_class: Type[UpdateSchemaType],
            data_schema_class: Type[DataSchemaType]
    ):
        self.model = model
        # Initialized Reponse Data
        self.create_protobuf_message_class = create_protobuf_message_class
        self.update_protobuf_message_class = update_protobuf_message_class
        self.single_protobuf_message_class = single_protobuf_message_class
        self.multi_protobuf_message_class = multi_protobuf_message_class
        self.create_schema_class = create_schema_class
        self.update_schema_class = update_schema_class
        self.data_schema_class = data_schema_class

    @property
    def objects(self) -> BaseQuerySet:
        """Get the objects property

        Returns:
            BaseQuerySet: QuerySet
        """
        return self.model.objects

    # Create ####################

    async def create(
        self,
        *,
        obj_in: CreateProtobufMessageType | CreateSchemaType | Dict[str, Any],
        extra_data: Dict[str, Any] = {},
        return_model: bool = False,
        **save_kwargs
    ) -> SingleDataProtobufMessageType | ModelType:

        if isinstance(obj_in, self.create_protobuf_message_class):
            data_in = self.create_schema_class.model_validate(
                MessageToDict(
                    obj_in,
                    use_integers_for_enums=False,
                    preserving_proto_field_name=True,
                    including_default_value_fields=True
                )
            ).model_dump()
        elif isinstance(obj_in, self.create_schema_class):
            data_in = obj_in.model_dump()
        else:
            data_in = obj_in

        data = {**data_in, **extra_data}
        logger.info(f"Data: {data}")

        db_obj = self.model(**data)

        db_obj.save(**save_kwargs)

        if return_model:
            return db_obj

        return self._purse_single_to_protobuf(db_obj)

    # Read #####################

    async def get_by_uuid(
        self,
        *,
        get_by_uuid_msg: base_pb2.GetByUUIDMsg,
        extra_filter: Dict[str, Any] = {},
        return_model: bool = False,
    ) -> SingleDataProtobufMessageType | ModelType:
        """Get the object by using the UUID

        Args:
            get_by_uuid_msg (GetByUUIDMessageType): GetByUUID message data
            return_model (bool): If True, the function will return model instance, else protobuf.

        Returns:
            SingleDataResponseMessageType: The response message
        """
        _q = {'uuid': get_by_uuid_msg.uuid, **extra_filter}

        logger.info(f"Get by UUID query: {_q}")
        db_obj = self.model.objects.get(**_q)
        if return_model:
            return db_obj

        return self._purse_single_to_protobuf(db_obj)

    async def get(
        self,
        *,
        get_query: base_pb2.GetQuery,
        ignore_unknown_fields: bool = True,
        extra_filter: Dict[str, Any] = {},
        return_model: bool = False,
    ) -> SingleDataProtobufMessageType | ModelType:
        """Get Document Based on query

        Args:
            get_query (base_pb2.GetQuery): Get Query message
            ignore_unknown_fields (bool, optional): If True, do not raise errors for unknown fields. Defaults to True.
            return_model (bool): If True, the function will return model instance, else protobuf.

        Returns:
            SingleDataResponseMessageType: The response message
        """
        # TODO: usage of Q is not done
        _q = {
            **MessageToDict(
                get_query.filter,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=False
            ),
            **extra_filter
        }

        logger.info(f"Get query: {_q}")
        db_obj = self.model.objects.get(**_q)
        if return_model:
            return db_obj

        return self._purse_single_to_protobuf(db_obj, ignore_unknown_fields)

    async def get_multi(
        self,
        *,
        multi_get_query: base_pb2.MultiGetQuery,
        extra_filter: Dict[str, Any] = {},
        return_model: bool = False
    ) -> MultiDataProtobufMessageType | List[ModelType]:
        """Get mutliple data based on the query

        Args:
            multi_get_query (base_pb2.MultiGetQuery): The get query model, should be a instance of the multi_get_query
            ignore_unknown_fields (bool, optional): If True, do not raise errors for unknown fields. Defaults to True.
            return_model (bool): If True, the function will return model instance, else protobuf.

        Returns:
            MultiDataResponseMessageType: Response from the database
        """

        _q = {**MessageToDict(multi_get_query.filter), **extra_filter}
        logger.info(f"Get Multi query: {_q}, skip: {multi_get_query.skip} limit: {multi_get_query.limit}")
        q = self.model.objects.filter(**_q).skip(multi_get_query.skip)
        if multi_get_query.limit != 0:
            q = q.limit(multi_get_query.limit)

        if return_model:
            return q

        return self._purse_multi_to_protobuf(q)

    async def update_one(
        self,
        *,
        db_obj: ModelType,
        obj_in: UpdateProtobufMessageType | UpdateSchemaType | Dict[str, Any],
        extra_update_data: Dict[str, Any] = {},
        return_model: bool = False,
        **kwargs
    ) -> ModelType | SingleDataProtobufMessageType:
        if isinstance(obj_in, self.update_protobuf_message_class):
            data_in = self.update_schema_class.model_validate(
                MessageToDict(
                    obj_in,
                    use_integers_for_enums=False,
                    preserving_proto_field_name=True,
                    including_default_value_fields=True
                )
            ).model_dump(exclude_none=True)
        elif isinstance(obj_in, self.update_schema_class):
            data_in = obj_in.model_dump(exclude_none=True)
        else:
            data_in = obj_in

        update_data = {**data_in, **extra_update_data}

        logger.info(f"Update New Data: {update_data}")

        update_document(db_obj, update_data)
        db_obj.save(**kwargs)
        db_obj.reload()

        if return_model:
            return db_obj

        return self._purse_single_to_protobuf(db_obj)

    async def remove_one(
        self,
        *,
        get_query: base_pb2.GetQuery,
        return_model: bool = False
    ) -> SingleDataProtobufMessageType | ModelType:
        """Remove the object from the db

        Args:
            get_query (base_pb2.GetQuery): Get Query message
            ignore_unknown_fields (bool, optional): If True, do not raise errors for unknown fields. Defaults to True.
            return_model (bool, optional): If True, the function will return model instance, else protobuf.
            Defaults to False.

        Returns:
            SingleDataResponseMessageType | ModelType: response from the database
        """
        db_obj = self.model.objects.get(**MessageToDict(
            get_query.filter,
            use_integers_for_enums=False,
            preserving_proto_field_name=True,
            including_default_value_fields=False
        ))
        db_obj.delete()
        if return_model:
            return db_obj

        return self._purse_single_to_protobuf(db_obj)

    async def remove_many(
        self,
        *,
        multi_get_query: base_pb2.MultiGetQuery,
        return_model: bool = False
    ) -> MultiDataProtobufMessageType | List[ModelType]:
        q = self.model.objects.filter(
            **MessageToDict(
                multi_get_query.filter,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=False
            )).skip(multi_get_query.skip)

        if multi_get_query.limit != 0:
            q = q.limit(multi_get_query.limit)
        q.delete()
        if return_model:
            return q

        return self._purse_multi_to_protobuf(q)

    def _purse_single_to_protobuf(
        self,
        db_obj: ModelType,
    ) -> SingleDataProtobufMessageType:
        return ParseDict(
            self.data_schema_class.model_validate(db_obj).model_dump(mode="json"),
            self.single_protobuf_message_class(),
            ignore_unknown_fields=True
        )

    def _purse_multi_to_protobuf(
        self,
        db_query_set: BaseQuerySet
    ) -> MultiDataProtobufMessageType:
        _data = pydantic.TypeAdapter(list[self.data_schema_class]).validate_python(db_query_set)
        return ParseDict(
            {'data': [
                self.data_schema_class.model_validate(d).model_dump(mode="json")
                for d in _data
            ]},
            self.multi_protobuf_message_class(),
            ignore_unknown_fields=True
        )
