from datetime import datetime, timezone
from datetime import date
from sqlalchemy import Date
from enum import Enum
from uuid import UUID,uuid4
from sqlalchemy import Boolean,DateTime,Enum as SQLEnum, ForeignKey,String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non-binary"
    OTHER = "other"

class Profile(Base):
    __tablename__="profiles"
    id:Mapped[UUID]=mapped_column(primary_key=True,default=uuid4)
    user_id:Mapped[UUID]=mapped_column(ForeignKey("users.id"),unique=True,nullable=False)
    first_name:Mapped[str]=mapped_column(String(225),nullable=False)
    last_name:Mapped[str]=mapped_column(String(225),nullable=False)
    birth_date:Mapped[date]=mapped_column(Date,nullable=False)
    bio:Mapped[str | None]=mapped_column(String(255),nullable=True)
    gender:Mapped[Gender]=mapped_column(SQLEnum(Gender),nullable=False)
    attracted_to:Mapped[str]=mapped_column(String(255),nullable=True)
    occupation:Mapped[str]=mapped_column(String(255),nullable=False)
    city:Mapped[str]=mapped_column(String(255),nullable=False)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))
    updated_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))
    pronouns:Mapped[str | None]=mapped_column(String(255),nullable=True)
    User=relationship("User",back_populates="profile")