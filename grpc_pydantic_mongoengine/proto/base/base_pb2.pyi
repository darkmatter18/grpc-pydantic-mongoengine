from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetByUUIDMsg(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class GetQuery(_message.Message):
    __slots__ = ("filter",)
    FILTER_FIELD_NUMBER: _ClassVar[int]
    filter: _struct_pb2.Struct
    def __init__(self, filter: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class MultiGetQuery(_message.Message):
    __slots__ = ("filter", "skip", "limit")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filter: _struct_pb2.Struct
    skip: int
    limit: int
    def __init__(self, filter: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., skip: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class UpdateRawQuery(_message.Message):
    __slots__ = ("filter", "data")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    filter: _struct_pb2.Struct
    data: _struct_pb2.Struct
    def __init__(self, filter: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CountMsg(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class MetadataMessage(_message.Message):
    __slots__ = ("etag", "created_on", "updated_on")
    ETAG_FIELD_NUMBER: _ClassVar[int]
    CREATED_ON_FIELD_NUMBER: _ClassVar[int]
    UPDATED_ON_FIELD_NUMBER: _ClassVar[int]
    etag: str
    created_on: str
    updated_on: str
    def __init__(self, etag: _Optional[str] = ..., created_on: _Optional[str] = ..., updated_on: _Optional[str] = ...) -> None: ...
