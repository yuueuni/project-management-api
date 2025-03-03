from pydantic import BaseModel, EmailStr

from app.enums.status_enum import SuccessFailExpireEnum


class SigninRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class SigninResponse(BaseModel):
    id: int

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str

class EmailRequest(BaseModel):
    email: EmailStr

class EmailVerifyRequest(BaseModel):
    email: EmailStr
    code: str

class EmailVerifyResponse(BaseModel):
    valid_result: SuccessFailExpireEnum

class PasswordResetRequest(BaseModel):
    email: EmailStr
    password: str


