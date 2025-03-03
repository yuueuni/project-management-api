from typing import Optional

from pydantic import BaseModel

from app.enums import RoleTypeEnum


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class CreateProjectRequest(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    project_id: int

class UpdateProjectRequest(ProjectBase):
    project_id: int

class AddProjectMemberRequest(BaseModel):
    member_id: int
    role: RoleTypeEnum
