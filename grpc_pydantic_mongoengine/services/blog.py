import grpc

from google.protobuf.empty_pb2 import Empty

from grpc_pydantic_mongoengine.proto.blog import blog_pb2_grpc, blog_pb2
from grpc_pydantic_mongoengine import crud


class BlogServicer(blog_pb2_grpc.BlogServicer):
    async def CreateBlog(
        self,
        request: blog_pb2.CreateBlogData,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        return await crud.crudblog.create(obj_in=request)

    async def GetBlogByUUID(
        self,
        request: blog_pb2.GetBlogByUUIDQuery,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        return await crud.crudblog.get_by_uuid(get_by_uuid_msg=request.blog)

    async def GetBlog(
        self,
        request: blog_pb2.GetBlogQuery,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        return await crud.crudblog.get(get_query=request.blog)

    async def GetMultiBlog(
        self,
        request: blog_pb2.MultiGetBlogQuery,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.MultiBlogData:
        return await crud.crudblog.get_multi(multi_get_query=request.blog)

    async def UpdateBlog(
        self,
        request: blog_pb2.UpdateBlogQuery,
        context: grpc.aio.ServicerContext
    ) -> blog_pb2.BlogData:
        model = await crud.crudblog.get(get_query=request.filter.blog, return_model=True)
        return await crud.crudblog.update_one(db_obj=model, obj_in=request.new_data)

    async def DeleteBlog(
        self,
        request: blog_pb2.GetBlogQuery,
        context: grpc.aio.ServicerContext
    ):
        await crud.crudblog.remove_one(get_query=request.blog)
        return Empty()

    async def DeleteMultiBlog(
        self,
        request: blog_pb2.MultiGetBlogQuery,
        context: grpc.aio.ServicerContext
    ):
        await crud.crudblog.remove_many(multi_get_query=request.blog)
        return Empty()
