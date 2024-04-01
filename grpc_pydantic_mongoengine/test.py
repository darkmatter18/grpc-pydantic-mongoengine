import asyncio
from uuid import uuid4

from grpc_pydantic_mongoengine.schemas.blog import BlogCreate, BlogUpdate, Publisher

from grpc_pydantic_mongoengine.rpc_client import blog

# Create
# out = asyncio.run(blog.create(
#     obj_in=BlogCreate(
#         title="Test",
#         description="sfdsfdasfdsfd",
#         created_by=uuid4(),
#         publised_via=Publisher.TYPE_A
#     )
# ))

# Get
# out = asyncio.run(blog.get(
#     uuid="15f6e676-71c0-4cef-ae50-0fa4305a3884"
# ))

# Get Multi
# out = asyncio.run(blog.get_multi())

# Get Multi with Query
# out = asyncio.run(blog.get_multi(
#     created_by='9f21a352-77f9-4d1f-ab07-c6c9b6caec26'
# ))

# Update
# out = asyncio.run(blog.update(
#     new_data=BlogUpdate(title="fasfsfasfasfd"),
#     created_by='9f21a352-77f9-4d1f-ab07-c6c9b6caec26'
# ))

# Get Meta Data
# out = asyncio.run(blog.get_metadata(
#     uuid="15f6e676-71c0-4cef-ae50-0fa4305a3884"
# ))

# print(out)
