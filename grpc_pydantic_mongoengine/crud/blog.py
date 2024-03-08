from .basegrpc import CRUDBaseGrpc

from grpc_pydantic_mongoengine import models, schemas
from grpc_pydantic_mongoengine.proto.blog import blog_pb2


class CRUDBlog(CRUDBaseGrpc[
    models.Blog,
    blog_pb2.CreateBlogData,
    blog_pb2.UpdateBlogData,
    blog_pb2.BlogData,
    blog_pb2.MultiBlogData,
    schemas.BlogCreate,
    schemas.BlogUpdate,
    schemas.Blog
]):
    pass


crudblog = CRUDBlog(
    model=models.Blog,
    create_protobuf_message_class=blog_pb2.CreateBlogData,
    update_protobuf_message_class=blog_pb2.UpdateBlogData,
    single_protobuf_message_class=blog_pb2.BlogData,
    multi_protobuf_message_class=blog_pb2.MultiBlogData,
    create_schema_class=schemas.BlogCreate,
    update_schema_class=schemas.BlogUpdate,
    data_schema_class=schemas.Blog
)
