from datetime import datetime, timezone
from enum import Enum
from uuid import UUID,uuid4
from sqlalchemy import Boolean,DateTime,Enum as SQLEnum,String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"
    id:Mapped[UUID]=mapped_column(primary_key=True,default=uuid4)
    email:Mapped[str]=mapped_column(String(255),unique=True,nullable=False, index=True)
    password_hash:Mapped[str]=mapped_column(String(255),nullable=False)
    role:Mapped[UserRole]=mapped_column(SQLEnum(UserRole),nullable=False,default=UserRole.USER)
    is_active:Mapped[bool]=mapped_column(Boolean,default=True)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))
    updated_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))
    