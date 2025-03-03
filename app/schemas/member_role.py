from pydantic import BaseModel

from app.enums import GrantRevokeEnum


class MemberRoleBase(BaseModel):
    member_id: int
    role_id: int
    target_id: int

class CreateMemberRole(BaseModel):
    created_by: int

class CreateMemberRoleHistory(MemberRoleBase):
    member_role_id: int
    action: GrantRevokeEnum
    created_at: str
    created_by: int
    updated_at: str
    updated_by: int
