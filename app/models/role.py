from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(50), nullable=False)
    role_name = Column(String(50), nullable=False)
    used = Column(String(1), nullable=False, default='Y')
