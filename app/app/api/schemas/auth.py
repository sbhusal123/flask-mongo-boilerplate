from marshmallow import Schema, fields, validates, ValidationError, \
    validates_schema


class AuthSchema(Schema):
    """Schema for POST request to get token"""
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    # validation for specific field
    # @validates("username")
    # def validate_username(self, value):
    #     if value == "":
    #         raise ValidationError("Username cannot be null")
    #     return value

    @validates_schema
    def validate_input(self, data, **kwargs):
        if data['username'] == "" or data["password"] == "":
            raise ValidationError("asdsad")


class AuthErrorResponseSchema(Schema):
    """Auth token error schema"""
    message = fields.Str()

class AuthTokenResponseSchema(Schema):
    """AUth token success schema"""
    token = fields.Str()
