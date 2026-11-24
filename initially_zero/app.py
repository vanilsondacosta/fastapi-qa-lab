from http import HTTPStatus

from fastapi import FastAPI

from initially_zero.schemas import (
    Message,
    UserDB,
    UserSchema,
    UserSchemaPublic,
)

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo!'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserSchemaPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        userName=user.userName,
        userEmail=user.userEmail,
        userPassword=user.userPassword,
        userId=len(database) + 1,
    )
    database.append(user_with_id)
    return user_with_id
