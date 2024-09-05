from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import User

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

class UserResponseSchema(UserSchema):
    class Meta(UserSchema.Meta):
        exclude = ("password", )