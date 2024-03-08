from google.protobuf import empty_pb2 as _empty_pb2
from grpc_pydantic_mongoengine.proto.base import base_pb2 as _base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Publisher(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUBLISHER_UNSPECIFIED: _ClassVar[Publisher]
    TYPE_A: _ClassVar[Publisher]
    TYPE_B: _ClassVar[Publisher]
    TYPE_C: _ClassVar[Publisher]
PUBLISHER_UNSPECIFIED: Publisher
TYPE_A: Publisher
TYPE_B: Publisher
TYPE_C: Publisher

class CreateBlogData(_message.Message):
    __slots__ = ("title", "description", "created_by", "publised_via")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    PUBLISED_VIA_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    created_by: str
    publised_via: Publisher
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., created_by: _Optional[str] = ..., publised_via: _Optional[_Union[Publisher, str]] = ...) -> None: ...

class UpdateBlogData(_message.Message):
    __slots__ = ("title", "description", "created_by", "publised_via")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    PUBLISED_VIA_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    created_by: str
    publised_via: Publisher
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., created_by: _Optional[str] = ..., publised_via: _Optional[_Union[Publisher, str]] = ...) -> None: ...

class BlogData(_message.Message):
    __slots__ = ("title", "description", "created_by", "created_on", "publised_via", "uuid")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    PUBLISED_VIA_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    created_by: str
    created_on: str
    publised_via: Publisher
    uuid: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., created_by: _Optional[str] = ..., created_on: _Optional[str] = ..., publised_via: _Optional[_Union[Publisher, str]] = ..., uuid: _Optional[str] = ...) -> None: ...

class MultiBlogData(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedCompositeFieldContainer[BlogData]
    def __init__(self, data: _Optional[_Iterable[_Union[BlogData, _Mapping]]] = ...) -> None: ...

class GetBlogByUUIDQuery(_message.Message):
    __slots__ = ("blog",)
    BLOG_FIELD_NUMBER: _ClassVar[int]
    blog: _base_pb2.GetByUUIDMsg
    def __init__(self, blog: _Optional[_Union[_base_pb2.GetByUUIDMsg, _Mapping]] = ...) -> None: ...

class GetBlogQuery(_message.Message):
    __slots__ = ("blog",)
    BLOG_FIELD_NUMBER: _ClassVar[int]
    blog: _base_pb2.GetQuery
    def __init__(self, blog: _Optional[_Union[_base_pb2.GetQuery, _Mapping]] = ...) -> None: ...

class MultiGetBlogQuery(_message.Message):
    __slots__ = ("blog",)
    BLOG_FIELD_NUMBER: _ClassVar[int]
    blog: _base_pb2.MultiGetQuery
    def __init__(self, blog: _Optional[_Union[_base_pb2.MultiGetQuery, _Mapping]] = ...) -> None: ...

class UpdateBlogQuery(_message.Message):
    __slots__ = ("new_data", "filter")
    NEW_DATA_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    new_data: UpdateBlogData
    filter: GetBlogQuery
    def __init__(self, new_data: _Optional[_Union[UpdateBlogData, _Mapping]] = ..., filter: _Optional[_Union[GetBlogQuery, _Mapping]] = ...) -> None: ...

class UpdateMultiBlogQuery(_message.Message):
    __slots__ = ("new_data", "filter")
    NEW_DATA_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    new_data: UpdateBlogData
    filter: MultiGetBlogQuery
    def __init__(self, new_data: _Optional[_Union[UpdateBlogData, _Mapping]] = ..., filter: _Optional[_Union[MultiGetBlogQuery, _Mapping]] = ...) -> None: ...
