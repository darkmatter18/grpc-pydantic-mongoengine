from grpc_pydantic_mongoengine.proto.blog import blog_pb2, blog_pb2_grpc
from grpc_pydantic_mongoengine import schemas
from .base_rpc_client import BaseRpcClient


class BlogRpcClient(BaseRpcClient):
    pass


blog = BlogRpcClient(
    url="localhost:50051",
    stub=blog_pb2_grpc.BlogStub,
    create_protobuf_message_class=blog_pb2.CreateBlogData,
    update_query_protobuf_message_class=blog_pb2.UpdateBlogQuery,
    single_protobuf_message_class=blog_pb2.BlogData,
    multi_protobuf_message_class=blog_pb2.MultiBlogData,
    create_schema_class=schemas.BlogCreate,
    update_schema_class=schemas.BlogUpdate,
    data_schema_class=schemas.Blog
)
