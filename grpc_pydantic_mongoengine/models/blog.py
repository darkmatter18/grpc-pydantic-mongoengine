from uuid import uuid4
from datetime import datetime

from mongoengine import Document, fields as _fields

from grpc_pydantic_mongoengine.schemas import Publisher


class Blog(Document):
    uuid = _fields.UUIDField(default=uuid4)
    title = _fields.StringField(required=True)
    description = _fields.StringField(required=True)
    created_by = _fields.UUIDField(required=True)
    created_on = _fields.DateTimeField(default=datetime.now)
    publised_via = _fields.EnumField(Publisher)
