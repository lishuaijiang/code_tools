from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
