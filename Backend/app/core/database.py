from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from app.core.config import settings

Database_URL=(f"postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}")
engine=create_engine(Database_URL,echo=True)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
class Base(DeclarativeBase):
    pass
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()