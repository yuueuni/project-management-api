from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import AuthService, MemberService,ProjectService


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)


def get_member_service(db: Session = Depends(get_db)) -> MemberService:
    return MemberService(db)

