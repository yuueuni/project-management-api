from typing import Type

from sqlalchemy.orm import Session

from app.models.member import Member
from app.schemas import SigninRequest, UpdateMemberRequest


class MemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_member_by_id(self, member_id: int) -> Type[Member] | None:
        return self.db.query(Member).filter(Member.id == member_id).first()

    def get_member_by_email(self, email: str) -> Type[Member] | None:
        return self.db.query(Member).filter(Member.email == email).first()

    def create_member(self, member_create: SigninRequest) -> Member:
        db_member = Member(
            name=member_create.name,
            email=member_create.email,
            password=member_create.password,
            created_by=1
        )
        self.db.add(db_member)
        return db_member

    def update_member_password(self, member: Member, password: str) -> Member:
        member.password = password
        self.db.add(member)
        return member

    def update_member(self, member: Member, member_update: UpdateMemberRequest) -> Member:
        member.name = member_update.name
        member.email = member_update.email
        self.db.add(member)
        return member