import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.session import get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    db = SessionLocal()
    db.begin()

    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture()
def override_get_db(db_session):
    def _get_db():
        return db_session

    app.dependency_overrides[get_db] = _get_db
    yield db_session
    del app.dependency_overrides[get_db]
