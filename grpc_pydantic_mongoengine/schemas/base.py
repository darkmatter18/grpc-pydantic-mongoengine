from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class MetaData(BaseModel):
    etag: UUID
    created_on: datetime
    updated_on: datetime
