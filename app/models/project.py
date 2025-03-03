from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text

from app.db.base import Base


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, comment='프로젝트명')
    description = Column(Text, comment='프로젝트 설명')
    used = Column(String(1), nullable=False, default='Y')
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    created_by = Column(Integer, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.now())
    updated_by = Column(Integer, nullable=True)

