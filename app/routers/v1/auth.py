from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.handler.response_handler import success_response
from app.dependencies.service_dependencies import get_auth_service
from app.schemas import SigninResponse, SigninRequest, LoginRequest, LoginResponse, PasswordResetRequest, \
    EmailVerifyResponse, EmailVerifyRequest, EmailRequest
from app.services import AuthService

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/swagger/token", status_code=200, description="로그인")
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        auth_service: AuthService = Depends(get_auth_service)
):
    return auth_service.login(
            LoginRequest(
                email=form_data.username,
                password=form_data.password
            )
        )

@auth_router.post("/signin", response_model=SigninResponse, status_code=201, description="회원가입")
async def signin(
        member: SigninRequest,
        auth_service: AuthService = Depends(get_auth_service)
):
    return success_response(data=auth_service.signin(member))

@auth_router.post("/login", response_model=LoginResponse, status_code=200, description="로그인")
async def login(
        login: LoginRequest,
        auth_service: AuthService = Depends(get_auth_service)
):
    return success_response(data=auth_service.login(login))

@auth_router.post("/email", status_code=200, description="이메일 전송")
async def send_email(
        email: EmailRequest,
        auth_service: AuthService = Depends(get_auth_service)
):
    return success_response(data=auth_service.send_email(email))

@auth_router.post("/email/verify", response_model=EmailVerifyResponse, status_code=200, description="이메일 인증")
async def verify_email(
        email_verify: EmailVerifyRequest,
        auth_service: AuthService = Depends(get_auth_service)
):
    return success_response(
        data=auth_service.verify_email(
            email=email_verify.email,
            code=email_verify.code
        )
    )

@auth_router.post("/password/reset", status_code=200, description="비밀번호 재설정")
async def reset_password(
        password: PasswordResetRequest,
        auth_service: AuthService = Depends(get_auth_service)
):
    return success_response(data=auth_service.reset_password(password))
