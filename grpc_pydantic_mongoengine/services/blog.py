import grpc

from google.protobuf.empty_pb2 import Empty

from grpc_pydantic_mongoengine.proto.base import base_pb2
from grpc_pydantic_mongoengine.proto.blog import blog_pb2_grpc, blog_pb2
from grpc_pydantic_mongoengine import crud


class BlogServicer(blog_pb2_grpc.BlogServicer):
    async def Create(
        self,
        request: blog_pb2.CreateBlogData,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        return await crud.crudblog.create(obj_in=request)

    async def GetByUUID(
        self,
        request: base_pb2.GetByUUIDMsg,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        return await crud.crudblog.get_by_uuid(get_by_uuid_msg=request)

    async def Get(
        self,
        request: base_pb2.GetQuery,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        return await crud.crudblog.get(get_query=request)

    async def GetMulti(
        self,
        request: base_pb2.MultiGetQuery,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.MultiBlogData:
        return await crud.crudblog.get_multi(multi_get_query=request)

    async def Update(
        self,
        request: blog_pb2.UpdateBlogQuery,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        model = await crud.crudblog.get(get_query=request.filter, return_model=True)
        return await crud.crudblog.update_one(db_obj=model, obj_in=request.new_data)

    async def Delete(
        self,
        request: base_pb2.GetQuery,
        context: grpc.aio.ServicerContext
    ):
        await crud.crudblog.remove_one(get_query=request.blog)
        return Empty()

    async def DeleteMulti(
        self,
        request: base_pb2.MultiGetQuery,
        context: grpc.aio.ServicerContext
    ):
        await crud.crudblog.remove_many(multi_get_query=request.blog)
        return Empty()
