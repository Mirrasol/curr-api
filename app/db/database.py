from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.DATABASE_URL)

session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    session = session_maker()
    try:
        yield session
    finally:
        session.close()
