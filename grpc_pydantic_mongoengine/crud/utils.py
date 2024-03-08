from datetime import datetime
from mongoengine.base import BaseDocument

from mongoengine import fields


def update_document(document: BaseDocument, data_dict: dict):

    def field_value(field, value):

        if field.__class__ in (fields.ListField, fields.SortedListField):
            return [field_value(field.field, item) for item in value]

        if field.__class__ in (
            fields.EmbeddedDocumentField,
            fields.GenericEmbeddedDocumentField
        ):
            return field.document_type(**value)

        if field.__class__ in (
            fields.DateField, fields.DateTimeField
        ):
            if isinstance(value, str):
                return datetime.fromisoformat(value)
            else:
                return value

        return value

    for key, value in data_dict.items():
        setattr(document, key, field_value(document._fields[key], value))

    return document
