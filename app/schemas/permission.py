from pydantic import BaseModel

from app.enums import HttpMethodEnum, PermissionTypeEnum

class PermissionBase(BaseModel):
    permission_name: str
    endpoint: str
    http_method: HttpMethodEnum
    permission_type: PermissionTypeEnum
    feature: str

class CreatePermission(PermissionBase):
    created_by: int

class CreatePermissionHistory(PermissionBase):
    permission_id: int
    created_at: str
    created_by: int
    updated_at: str
    updated_by: int

