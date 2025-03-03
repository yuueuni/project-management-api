from fastapi import APIRouter

from .projects import project_router
from .members import member_router
from .auth import auth_router

router = APIRouter(prefix="/v1")
router.include_router(project_router)
router.include_router(member_router)
router.include_router(auth_router)
