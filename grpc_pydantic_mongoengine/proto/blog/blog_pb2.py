# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_pydantic_mongoengine/proto/blog/blog.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from grpc_pydantic_mongoengine.proto.base import base_pb2 as grpc__pydantic__mongoengine_dot_proto_dot_base_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/grpc_pydantic_mongoengine/proto/blog/blog.proto\x12\x1egrpc_pydantic_mongoengine.blog\x1a\x1bgoogle/protobuf/empty.proto\x1a/grpc_pydantic_mongoengine/proto/base/base.proto\"\x89\x01\n\x0e\x43reateBlogData\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\ncreated_by\x18\x03 \x01(\t\x12?\n\x0cpublised_via\x18\x04 \x01(\x0e\x32).grpc_pydantic_mongoengine.blog.Publisher\"\xd7\x01\n\x0eUpdateBlogData\x12\x12\n\x05title\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\ncreated_by\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x44\n\x0cpublised_via\x18\x04 \x01(\x0e\x32).grpc_pydantic_mongoengine.blog.PublisherH\x03\x88\x01\x01\x42\x08\n\x06_titleB\x0e\n\x0c_descriptionB\r\n\x0b_created_byB\x0f\n\r_publised_via\"\xa5\x01\n\x08\x42logData\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\ncreated_by\x18\x03 \x01(\t\x12\x12\n\ncreated_on\x18\x04 \x01(\t\x12?\n\x0cpublised_via\x18\x05 \x01(\x0e\x32).grpc_pydantic_mongoengine.blog.Publisher\x12\x0c\n\x04uuid\x18\x06 \x01(\t\"G\n\rMultiBlogData\x12\x36\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32(.grpc_pydantic_mongoengine.blog.BlogData\"\x8d\x01\n\x0fUpdateBlogQuery\x12@\n\x08new_data\x18\x01 \x01(\x0b\x32..grpc_pydantic_mongoengine.blog.UpdateBlogData\x12\x38\n\x06\x66ilter\x18\x02 \x01(\x0b\x32(.grpc_pydantic_mongoengine.base.GetQuery\"\x97\x01\n\x14UpdateMultiBlogQuery\x12@\n\x08new_data\x18\x01 \x01(\x0b\x32..grpc_pydantic_mongoengine.blog.UpdateBlogData\x12=\n\x06\x66ilter\x18\x02 \x01(\x0b\x32-.grpc_pydantic_mongoengine.base.MultiGetQuery*J\n\tPublisher\x12\x19\n\x15PUBLISHER_UNSPECIFIED\x10\x00\x12\n\n\x06TYPE_A\x10\x01\x12\n\n\x06TYPE_B\x10\x02\x12\n\n\x06TYPE_C\x10\x03\x32\xfd\x05\n\x04\x42log\x12\x62\n\x06\x43reate\x12..grpc_pydantic_mongoengine.blog.CreateBlogData\x1a(.grpc_pydantic_mongoengine.blog.BlogData\x12\x63\n\tGetByUUID\x12,.grpc_pydantic_mongoengine.base.GetByUUIDMsg\x1a(.grpc_pydantic_mongoengine.blog.BlogData\x12Y\n\x03Get\x12(.grpc_pydantic_mongoengine.base.GetQuery\x1a(.grpc_pydantic_mongoengine.blog.BlogData\x12h\n\x08GetMulti\x12-.grpc_pydantic_mongoengine.base.MultiGetQuery\x1a-.grpc_pydantic_mongoengine.blog.MultiBlogData\x12\x63\n\x06Update\x12/.grpc_pydantic_mongoengine.blog.UpdateBlogQuery\x1a(.grpc_pydantic_mongoengine.blog.BlogData\x12J\n\x06\x44\x65lete\x12(.grpc_pydantic_mongoengine.base.GetQuery\x1a\x16.google.protobuf.Empty\x12T\n\x0b\x44\x65leteMulti\x12-.grpc_pydantic_mongoengine.base.MultiGetQuery\x1a\x16.google.protobuf.Empty\x12`\n\x05\x43ount\x12-.grpc_pydantic_mongoengine.base.MultiGetQuery\x1a(.grpc_pydantic_mongoengine.base.CountMsgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pydantic_mongoengine.proto.blog.blog_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PUBLISHER']._serialized_start=1058
  _globals['_PUBLISHER']._serialized_end=1132
  _globals['_CREATEBLOGDATA']._serialized_start=162
  _globals['_CREATEBLOGDATA']._serialized_end=299
  _globals['_UPDATEBLOGDATA']._serialized_start=302
  _globals['_UPDATEBLOGDATA']._serialized_end=517
  _globals['_BLOGDATA']._serialized_start=520
  _globals['_BLOGDATA']._serialized_end=685
  _globals['_MULTIBLOGDATA']._serialized_start=687
  _globals['_MULTIBLOGDATA']._serialized_end=758
  _globals['_UPDATEBLOGQUERY']._serialized_start=761
  _globals['_UPDATEBLOGQUERY']._serialized_end=902
  _globals['_UPDATEMULTIBLOGQUERY']._serialized_start=905
  _globals['_UPDATEMULTIBLOGQUERY']._serialized_end=1056
  _globals['_BLOG']._serialized_start=1135
  _globals['_BLOG']._serialized_end=1900
# @@protoc_insertion_point(module_scope)
