import string
from datetime import datetime
from random import random

from passlib.handlers.sha2_crypt import sha256_crypt
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.repositories import MemberRepository
from app.repositories.auth_repository import AuthRepository
from app.schemas import SigninResponse, SigninRequest, LoginResponse, LoginRequest


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.member_repository = MemberRepository(db)
        self.auth_repository = AuthRepository(db)
        self.authenticated_expire_minutes = 5

    def signin(self, member: SigninRequest) -> SigninResponse:
        try:
            if self.member_repository.get_member_by_email(member.email):
                raise Exception("이미 등록된 이메일 입니다.")
            member.password = sha256_crypt.hash(member.password)
            new_member = self.member_repository.create_member(member)
            self.db.commit()
            return SigninResponse(
                id=new_member.id
            )
        except Exception as e:
            self.db.rollback()
            raise e

    def login(self, login: LoginRequest) -> LoginResponse:
        member = self.member_repository.get_member_by_email(login.email)
        if not member:
            raise Exception("등록되지 않은 이메일 입니다.")
        if not sha256_crypt.verify(login.password, member.password):
            raise Exception("비밀번호가 일치하지 않습니다.")
        return LoginResponse(
            access_token=create_access_token(
                data={
                    "sub": member.email
                }
            ),
            token_type="bearer"
        )

    def send_email(self, email):
        try:
            # TODO send email
            email_code = self.auth_repository.create_email_code(
                email=email,
                code=self.__random_string_generator(size=6),
                expired_at=datetime.timedelta(minutes=self.authenticated_expire_minutes)
            )
            self.db.commit()
            return email_code
        except Exception as e:
            self.db.rollback()
            raise e

    def __random_string_generator(self, size: int = 6):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))

    def verify_email(self, email: str, code: str) -> bool:
        email_code = self.auth_repository.get_email_code_by_email(email=email, code=code)
        if not email_code:
            raise Exception("인증 코드가 존재하지 않습니다.")
        if email_code.expired_at < datetime.now():
            raise Exception("인증 코드가 만료되었습니다.")
        return True

    def reset_password(self, password):
        try:
            member = self.member_repository.get_member_by_email(password.email)
            if not member:
                raise Exception("등록되지 않은 이메일 입니다.")
            hash_password = sha256_crypt.hash(password.password)
            if member.password == hash_password:
                raise Exception("기존 비밀번호와 동일합니다.")
            self.member_repository.update_member_password(password=hash_password)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise e
