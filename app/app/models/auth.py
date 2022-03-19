import mongoengine as me


class User(me.Document):
    username = me.StringField(required=True)
    password = me.StringField(required=True)

    def validate(self, clean=True):
        """Any model level validation logic here"""
        return super().validate(clean)
