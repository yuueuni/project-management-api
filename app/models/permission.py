from sqlalchemy import Column, Integer, String, DateTime, func

from app.db.base import Base


class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True, index=True)
    permission_name = Column(String(100), unique=True, nullable=False)
    endpoint = Column(String(255), nullable=False)
    http_method = Column(String(10), nullable=False)
    permission_type = Column(String(20), nullable=False)
    feature = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    updated_by = Column(Integer, nullable=True)
