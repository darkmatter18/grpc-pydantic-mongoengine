# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_pydantic_mongoengine/proto/base/base.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/grpc_pydantic_mongoengine/proto/base/base.proto\x12\x1egrpc_pydantic_mongoengine.base\x1a\x1cgoogle/protobuf/struct.proto\"\x1c\n\x0cGetByUUIDMsg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"3\n\x08GetQuery\x12\'\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x82\x01\n\rMultiGetQuery\x12,\n\x06\x66ilter\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x12\x11\n\x04skip\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\x05limit\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\t\n\x07_filterB\x07\n\x05_skipB\x08\n\x06_limit\"\x19\n\x08\x43ountMsg\x12\r\n\x05\x63ount\x18\x01 \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pydantic_mongoengine.proto.base.base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETBYUUIDMSG']._serialized_start=113
  _globals['_GETBYUUIDMSG']._serialized_end=141
  _globals['_GETQUERY']._serialized_start=143
  _globals['_GETQUERY']._serialized_end=194
  _globals['_MULTIGETQUERY']._serialized_start=197
  _globals['_MULTIGETQUERY']._serialized_end=327
  _globals['_COUNTMSG']._serialized_start=329
  _globals['_COUNTMSG']._serialized_end=354
# @@protoc_insertion_point(module_scope)
