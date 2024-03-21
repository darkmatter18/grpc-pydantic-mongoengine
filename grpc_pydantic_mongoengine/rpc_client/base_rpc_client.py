import uuid
from typing import Any, Dict, Generic, Type, TypeVar

import grpc
from pydantic import BaseModel, TypeAdapter

from google.protobuf.message import Message
from google.protobuf.struct_pb2 import Struct
from google.protobuf.json_format import MessageToDict

from grpc_pydantic_mongoengine.proto.base import base_pb2

# Protobuf Model Types
CreateDataProtobufMessageType = TypeVar("CreateDataProtobufMessageType", bound=Message)
UpdateDataProtobufMessageType = TypeVar("UpdateDataProtobufMessageType", bound=Message)
UpdateQueryProtobufMessageType = TypeVar("UpdateQueryProtobufMessageType", bound=Message)
SingleDataProtobufMessageType = TypeVar("SingleDataProtobufMessageType", bound=Message)
MultiDataProtobufMessageType = TypeVar("MultiDataProtobufMessageType", bound=Message)

# Pydantic Schema Types
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
DataSchemaType = TypeVar("DataSchemaType", bound=BaseModel)


class BaseRpcClient(
    Generic[
        CreateDataProtobufMessageType,
        UpdateDataProtobufMessageType,
        UpdateQueryProtobufMessageType,
        SingleDataProtobufMessageType,
        MultiDataProtobufMessageType,
        CreateSchemaType,
        UpdateSchemaType,
        DataSchemaType
    ]
):
    def __init__(
        self,
        *,
        url: str,
        stub: object,
        create_data_protobuf_message_class: Type[CreateDataProtobufMessageType],
        update_data_protobuf_message_class: Type[UpdateDataProtobufMessageType],
        update_query_protobuf_message_class: Type[UpdateQueryProtobufMessageType],
        single_data_protobuf_message_class: Type[SingleDataProtobufMessageType],
        multi_data_protobuf_message_class: Type[MultiDataProtobufMessageType],
        create_schema_class: Type[CreateSchemaType],
        update_schema_class: Type[UpdateSchemaType],
        data_schema_class: Type[DataSchemaType]
    ) -> None:
        self._url = url
        self._stub = stub
        self._create_data_protobuf_message_class = create_data_protobuf_message_class
        self._update_data_protobuf_message_class = update_data_protobuf_message_class
        self._update_query_protobuf_message_class = update_query_protobuf_message_class
        self._single_data_protobuf_message_class = single_data_protobuf_message_class
        self._multi_data_protobuf_message_class = multi_data_protobuf_message_class
        self._create_schema_class = create_schema_class
        self._update_schema_class = update_schema_class
        self._data_schema_class = data_schema_class

    async def create(
        self,
        *,
        obj_in: CreateSchemaType
    ) -> DataSchemaType:
        async with grpc.aio.insecure_channel(self._url) as channel:
            stub = self._stub(channel)
            resp: self._single_data_protobuf_message_class = await stub.Create(
                self._create_data_protobuf_message_class(**obj_in.model_dump(mode="json"))
            )
            return self._data_schema_class.model_validate(MessageToDict(
                resp,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            ))

    async def get_by_uuid(
        self,
        *,
        uuid: uuid.UUID
    ) -> DataSchemaType:
        async with grpc.aio.insecure_channel(self._url) as channel:
            stub = self._stub(channel)
            resp: self._single_data_protobuf_message_class = await stub.GetByUUID(
                base_pb2.GetByUUIDMsg(uuid=str(uuid))
            )
            return self._data_schema_class.model_validate(MessageToDict(
                resp,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            ))

    async def get(
        self,
        **query
    ) -> DataSchemaType:
        async with grpc.aio.insecure_channel(self._url) as channel:
            s = Struct()
            s.update(query)
            stub = self._stub(channel)
            resp: self._single_data_protobuf_message_class = await stub.Get(
                blog=base_pb2.GetQuery(filter=s)
            )
            return self._data_schema_class.model_validate(MessageToDict(
                resp,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            ))

    async def get_multi(
        self,
        *,
        skip: int | None = None,
        limit: int | None = None,
        **query,
    ) -> list[DataSchemaType]:
        async with grpc.aio.insecure_channel(self._url) as channel:
            s = Struct()
            s.update(query)
            stub = self._stub(channel)
            resp: self._multi_data_protobuf_message_class = await stub.GetMulti(
                base_pb2.MultiGetQuery(
                    filter=s,
                    skip=skip,
                    limit=limit
                )
            )
            return TypeAdapter(list[self._data_schema_class]).validate_python(MessageToDict(
                resp,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            )['data'])

    async def update(
        self,
        *,
        new_data: UpdateSchemaType,
        **query
    ) -> DataSchemaType:
        s = Struct()
        s.update(query)
        async with grpc.aio.insecure_channel(self._url) as channel:
            stub = self._stub(channel)
            resp: self._single_data_protobuf_message_class = await stub.Update(
                self._update_query_protobuf_message_class(
                    new_data=self._update_data_protobuf_message_class(
                        **new_data.model_dump(mode="json")
                    ),
                    filter=base_pb2.GetQuery(filter=s)
                )
            )
            return self._data_schema_class.model_validate(MessageToDict(
                resp,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            ))

    async def update_raw(
        self,
        *,
        query: Dict[str, Any],
        **raw_update
    ) -> DataSchemaType:
        s = Struct()
        s.update(query)
        r = Struct()
        r.update(raw_update)
        async with grpc.aio.insecure_channel(self._url) as channel:
            stub = self._stub(channel)
            resp: self._single_data_protobuf_message_class = await stub.UpdateRaw(
                base_pb2.UpdateRawQuery(
                    filter=s,
                    data=r
                )
            )
            return TypeAdapter(list[self._data_schema_class]).validate_python(MessageToDict(
                resp,
                use_integers_for_enums=False,
                preserving_proto_field_name=True,
                including_default_value_fields=True
            )['data'])

    async def delete(self, **query):
        s = Struct()
        s.update(query)
        async with grpc.aio.insecure_channel(self._url) as channel:
            stub = self._stub(channel)
            await stub.Delete(
                base_pb2.GetQuery(filter=s)
            )

    async def delete_many(self, **query):
        s = Struct()
        s.update(query)
        async with grpc.aio.insecure_channel(self._url) as channel:
            stub = self._stub(channel)
            await stub.DeleteMulti(
                base_pb2.MultiGetQuery(filter=s)
            )

    async def count(self, **query) -> int:
        s = Struct()
        s.update(query)
        async with grpc.aio.insecure_channel(self._url) as channel:
            stub = self._stub(channel)
            count: base_pb2.CountMsg = stub.Count(
                base_pb2.MultiGetQuery(filter=s)
            )
            return count.count
