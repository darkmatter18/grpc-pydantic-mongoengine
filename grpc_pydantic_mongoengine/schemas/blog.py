from enum import Enum
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from grpc_pydantic_mongoengine.schemas.base import MetaData


class Publisher(Enum):
    TYPE_A = "TYPE_A"
    TYPE_B = "TYPE_B"
    TYPE_C = "TYPE_C"


class BlogBase(BaseModel):
    title: str | None = Field(None)
    description: str | None = Field(None)
    created_by: UUID | None = Field(None)
    publised_via: Publisher | None = Field(None)


class BlogCreate(BlogBase):
    title: str = Field(...)
    description: str = Field(...)
    created_by: UUID = Field(...)
    publised_via: Publisher = Field(...)


class BlogUpdate(BlogBase):
    pass


class BlogOnDB(BlogBase):
    metadata: MetaData = Field(...)
    uuid: UUID = Field(...)
    title: str = Field(...)
    description: str = Field(...)
    created_by: UUID = Field(...)
    created_on: datetime = Field(...)
    publised_via: Publisher = Field(...)

    model_config = ConfigDict(from_attributes=True)


class Blog(BlogOnDB):
    pass
