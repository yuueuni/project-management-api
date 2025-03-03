from sqlalchemy.orm import Session

from app.repositories import MemberRepository
from app.schemas.member import MemberResponse


class MemberService:
    def __init__(self, db: Session):
        self.db = db
        self.member_repository = MemberRepository(db)

    def get_member(self, member_id) -> MemberResponse:
        member = self.member_repository.get_member_by_id(member_id)
        return MemberResponse(
            id=member.id,
            name=member.name,
            email=member.email
        )

    def update_member_password(self, member_id, password) -> MemberResponse:
        member = self.member_repository.get_member_by_id(member_id)
        member = self.member_repository.update_member_password(member, password)
        self.db.commit()
        return MemberResponse(
            id=member.id,
            name=member.name,
            email=member.email
        )

    def update_member(self, member_id, member_update) -> MemberResponse:
        member = self.member_repository.get_member_by_id(member_id)
        member = self.member_repository.update_member(member, member_update)
        self.db.commit()
        return MemberResponse(
            id=member.id,
            name=member.name,
            email=member.email
        )

    def delete_member(self, member_id):
        member = self.member_repository.get_member_by_id(member_id)
        self.member_repository.delete_member(member)
        self.db.commit()
