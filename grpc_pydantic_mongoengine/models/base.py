from mongoengine import EmbeddedDocument, UUIDField, DateTimeField


class MetaDataEmbedDocument(EmbeddedDocument):
    etag = UUIDField()
    created_on = DateTimeField()
    updated_on = DateTimeField()
