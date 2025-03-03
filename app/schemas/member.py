from pydantic import BaseModel, EmailStr


class MemberBase(BaseModel):
    name: str
    email: EmailStr

class MemberResponse(MemberBase):
    id: int

class UpdateMemberRequest(MemberBase):
    password: str

