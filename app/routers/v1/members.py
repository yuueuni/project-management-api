from fastapi import APIRouter, Depends

from app.core.handler.response_handler import success_response
from app.core.jwt import oauth2_scheme
from app.dependencies.service_dependencies import get_member_service
from app.schemas import MemberResponse, UpdateMemberRequest
from app.services.member_service import MemberService

member_router = APIRouter(prefix="/members", tags=["members"])


@member_router.get(path="/{member_id}", response_model=MemberResponse, description="Get Member")
def get_member(
        member_id: int,
        token: str = Depends(oauth2_scheme),
        member_service: MemberService = Depends(get_member_service)
):
    return success_response(data=member_service.get_member(member_id))

@member_router.put(path="/{member_id}", response_model=MemberResponse, description="Update Member")
def update_member(
        member_id: int,
        member: UpdateMemberRequest,
        member_service: MemberService = Depends(get_member_service)
):
    return success_response(data=member_service.update_member(member_id, member))

@member_router.delete(path="/{member_id}", response_model=MemberResponse, description="Delete Member")
def delete_member(
        member_id: int,
        member_service: MemberService = Depends(get_member_service)
):
    return success_response(data=member_service.delete_member(member_id))
