from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db.base import Base


class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    created_by = Column(Integer, nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())
    updated_by = Column(Integer, nullable=True)
