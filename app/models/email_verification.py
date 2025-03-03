from sqlalchemy import Column, Integer, DateTime, func, String

from app.db.base import Base


class EmailVerification(Base):
    __tablename__ = 'email_verification'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    code = Column(String(6), nullable=False)
    expired_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

