from pydantic import BaseModel

from app.enums import RoleTypeEnum, UsedYseNoEnum


class RoleBase(BaseModel):
    role: RoleTypeEnum
    role_name: str
    used: UsedYseNoEnum

class CreateRole(BaseModel):
    role: RoleTypeEnum
    role_name: str
    used: UsedYseNoEnum

class CreateRolePermission(BaseModel):
    role_id: int
    permission_id: int
