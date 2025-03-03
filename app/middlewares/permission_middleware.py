from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.core.config import settings
from app.db.session import SessionLocal
from app.models import Member
from app.models.permission import Permission


class PermissionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        if request.url.path in settings.EXCLUDED_PATHS:
            return await call_next(request)

        if not hasattr(request.state, "user") or "email" not in request.state.user:
            raise HTTPException(status_code=403, detail="Authentication required")

        email = request.state.user["email"]
        db: Session = SessionLocal()

        try:
            user = db.query(Member).filter(Member.email == email).first()
            if not user:
                raise HTTPException(status_code=403, detail="User not found")

            # Permission(id, endpoint, method) - Role-Permission(id, role_id, permission_id) - Member-Role(id, member_id, role_id)
            per = db.query(Permission).filter(
                Permission.endpoint == request.url.path,
                Permission.method == request.method
            ).join(Permission.roles).join(Permission.roles.members).filter(Member.id == user.id).first()

            permission = db.query(Permission).filter(
                Permission.endpoint == request.url.path,
                Permission.method == request.method
            ).first()
            if not permission:
                raise HTTPException(status_code=403, detail="Permission denied")
        finally:
            db.close()

        return await call_next(request)
