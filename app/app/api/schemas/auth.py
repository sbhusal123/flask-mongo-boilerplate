from marshmallow import Schema, fields, validates, ValidationError


class AuthSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @validates("username")
    def validate_username(self, value):
        if value == "":
            raise ValidationError("Username cannot be null")