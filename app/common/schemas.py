from marshmallow import Schema, fields


class ErrorResponseSchema(Schema):
    """Auth token error schema"""
    message = fields.Str()
