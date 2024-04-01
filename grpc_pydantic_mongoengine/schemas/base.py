from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict


class MetaData(BaseModel):
    etag: UUID
    created_on: datetime
    updated_on: datetime

    model_config = ConfigDict(from_attributes=True)
