from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey,Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class MessageType(Enum):
    TEXT="text"
    SYSTEM="system"
    IMAGE="image"
    LINK="link"

class Message(Base):
    __tablename__="messages"
    id:Mapped[UUID]=mapped_column(primary_key=True, default=uuid4)
    conversation_id:Mapped[UUID]=mapped_column(ForeignKey("conversations.id"),nullable=False)
    sender_id:Mapped[UUID]=mapped_column(ForeignKey("users.id"),nullable=False)
    content:Mapped[str]=mapped_column(Text,nullable=False)
    type:Mapped[MessageType]=mapped_column(SQLEnum(MessageType),nullable=False,default=MessageType.TEXT)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))
    updated_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc),onupdate=lambda: datetime.now(timezone.utc))