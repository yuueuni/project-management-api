from fastapi import APIRouter, Depends

from app.core.handler.response_handler import success_response
from app.dependencies.service_dependencies import get_project_service
from app.schemas import AddProjectMemberRequest, UpdateProjectRequest, \
    ProjectResponse, CreateProjectRequest
from app.services import ProjectService

project_router = APIRouter(prefix="/projects", tags=["project"])

@project_router.post("/", response_model=ProjectResponse, status_code=201, description="프로젝트 생성")
async def create_project(
        project: CreateProjectRequest,
        project_service: ProjectService = Depends(get_project_service)
):
    return success_response(data=project_service.create_project(project))

@project_router.get("/{project_id}", response_model=ProjectResponse, status_code=200, description="프로젝트 조회")
async def get_project(
        project_id: int,
        project_service: ProjectService = Depends(get_project_service)
):
    return success_response(data=project_service.get_project_by_id(project_id))

@project_router.put("/{project_id}", response_model=ProjectResponse, status_code=200, description="프로젝트 수정")
async def update_project(
        project: UpdateProjectRequest,
        project_service: ProjectService = Depends(get_project_service)
):
    return success_response(data=project_service.update_project(project))

@project_router.delete("/{project_id}", status_code=200, description="프로젝트 삭제")
async def delete_project(
        project_id: int,
        project_service: ProjectService = Depends(get_project_service)
):
    return success_response(data=project_service.delete_project(project_id))

@project_router.post("/{project_id}/invite", status_code=200, description="프로젝트 멤버 추가")
async def add_project_member(
        project_id: int,
        add_project_member_request: AddProjectMemberRequest,
        project_service: ProjectService = Depends(get_project_service)
):
    return success_response(data=project_service.add_project_member(project_id, add_project_member_request))

