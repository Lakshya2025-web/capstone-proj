from ninja import Schema
class LoginSchema(Schema):
    username: str
    password: str

class TokenSchema(Schema):
    access: str
    refresh: str

class SignUpSchema(Schema):
    username: str
    password1 : str
    password2 : str
    email : str