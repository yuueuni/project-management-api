from sqlalchemy import Column, Integer, DateTime, func, ForeignKey

from app.db.base import Base


class MemberRole(Base):
    __tablename__ = 'member_role'

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('member.id'), nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    target_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    updated_by = Column(Integer, nullable=True)
