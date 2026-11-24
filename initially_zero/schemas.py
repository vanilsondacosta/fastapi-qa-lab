from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    userName: str
    userEmail: EmailStr
    userPassword: str


class UserSchemaPublic(BaseModel):
    userName: str
    userEmail: EmailStr
    userId: int


class UserDB(UserSchema):
    userId: int
