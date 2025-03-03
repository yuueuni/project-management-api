from sqlalchemy import Column, Integer, DateTime, func, ForeignKey

from app.db.base import Base


class RolePermission(Base):
    __tablename__ = 'role_permission'

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    permission_id = Column(Integer, ForeignKey('permission.id'), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    updated_by = Column(Integer, nullable=True)
