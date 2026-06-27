from datetime import datetime
from enum import Enum
from uuid import UUID,uuid4
from sqlalchemy import Boolean,DateTime,Enum as SQLEnum,String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    