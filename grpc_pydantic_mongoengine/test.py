import asyncio
from uuid import uuid4

from grpc_pydantic_mongoengine.schemas.blog import BlogCreate, Publisher

from grpc_pydantic_mongoengine.rpc_client import blog


out = asyncio.run(blog.create(
    obj_in=BlogCreate(
        title="Test",
        description="sfdsfdasfdsfd",
        created_by=uuid4(),
        publised_via=Publisher.TYPE_A
    )
))

print(out)
