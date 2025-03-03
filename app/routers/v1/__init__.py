from fastapi import APIRouter

from .auth import auth_router

router = APIRouter(prefix="/v1")
router.include_router(auth_router)
