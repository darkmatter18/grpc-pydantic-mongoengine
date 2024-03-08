import uuid

import grpc
from pydantic import TypeAdapter
from google.protobuf.struct_pb2 import Struct

from grpc_pydantic_mongoengine.proto.base import base_pb2
from grpc_pydantic_mongoengine.proto.blog import blog_pb2, blog_pb2_grpc

from grpc_pydantic_mongoengine import schemas


class Blog:
    def __init__(self) -> None:
        self.url = "localhost:50051"

    async def create(
        self,
        *,
        obj_in: schemas.BlogCreate
    ) -> schemas.Blog:
        print(obj_in.model_dump(mode="json"))
        async with grpc.aio.insecure_channel(self.url) as channel:
            stub = blog_pb2_grpc.BlogStub(channel)
            resp: blog_pb2.BlogData = await stub.CreateBlog(
                blog_pb2.CreateBlogData(**obj_in.model_dump(mode="json"))
            )
            return schemas.Blog.model_validate(resp)

    async def get_by_uuid(
        self,
        *,
        uuid: uuid.UUID
    ) -> schemas.Blog:
        async with grpc.aio.insecure_channel(self.url) as channel:
            stub = blog_pb2_grpc.BlogStub(channel)
            resp: blog_pb2.BlogData = await stub.GetProductByUUID(
                blog_pb2.GetBlogByUUIDQuery(
                    blog=base_pb2.GetByUUIDMsg(uuid=str(uuid))
                )
            )
            return schemas.Blog.model_validate(resp)

    async def get(
        self,
        **query
    ) -> schemas.Blog:
        async with grpc.aio.insecure_channel(self.url) as channel:
            s = Struct()
            s.update(query)
            stub = blog_pb2_grpc.BlogStub(channel)
            resp: blog_pb2.BlogData = await stub.GetBlog(
                blog_pb2.GetBlogQuery(
                    blog=base_pb2.GetQuery(filter=s)
                )
            )
            return schemas.Blog.model_validate(resp)

    async def get_multi(
        self,
        *,
        skip: int | None = None,
        limit: int | None = None,
        **query,
    ) -> list[schemas.Blog]:
        async with grpc.aio.insecure_channel(self.url) as channel:
            s = Struct()
            s.update(query)
            stub = blog_pb2_grpc.BlogStub(channel)
            resp: blog_pb2.MultiBlogData = await stub.GetMultiBlog(
                blog_pb2.MultiGetBlogQuery(
                    blog=base_pb2.MultiGetQuery(
                        filter=s,
                        skip=skip,
                        limit=limit
                    )
                )
            )
            return TypeAdapter(list[schemas.Blog]).validate_python(resp)

    async def update(
        self,
        *,
        new_data: schemas.BlogUpdate,
        **query
    ) -> schemas.Blog:
        s = Struct()
        s.update(query)
        async with grpc.aio.insecure_channel(self.url) as channel:
            stub = blog_pb2_grpc.BlogStub(channel)
            resp: blog_pb2.BlogData = await stub.UpdateBlog(
                blog_pb2.UpdateBlogQuery(
                    new_data=blog_pb2.UpdateBlogData(
                        **new_data.model_dump(mode="json")
                    ),
                    filter=blog_pb2.GetBlogQuery(
                        blog=base_pb2.GetQuery(filter=s)
                    )
                )
            )
            return schemas.Blog.model_validate(resp)

    async def delete(self, **query):
        s = Struct()
        s.update(query)
        async with grpc.aio.insecure_channel(self.url) as channel:
            stub = blog_pb2_grpc.BlogStub(channel)
            await stub.DeleteBlog(
                blog_pb2.GetBlogQuery(
                    blog=base_pb2.GetQuery(filter=s)
                )
            )

    async def delete_many(self, **query):
        s = Struct()
        s.update(query)
        async with grpc.aio.insecure_channel(self.url) as channel:
            stub = blog_pb2_grpc.BlogStub(channel)
            await stub.DeleteMultiBlog(
                blog_pb2.MultiGetBlogQuery(
                    blog=base_pb2.MultiGetQuery(filter=s)
                )
            )


blog = Blog()
