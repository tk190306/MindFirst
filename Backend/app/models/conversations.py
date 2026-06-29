from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey,CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.core.database import Base

class ConversationStatus(Enum):
    ACTIVE_ANONYMOUS="active_anonymous"
    REVEAL_PENDING="reveal_pending"
    ACTIVE_REVEALED="active_revealed"

class Conversation(Base):
    __tablename__="conversations"
    __table_args__=(
        CheckConstraint("user1_id <> user2_id", name="check_user1_user2_different"),
    )
    id:Mapped[UUID]=mapped_column(primary_key=True, default=uuid4)
    user1_id:Mapped[UUID]=mapped_column(ForeignKey("users.id"),nullable=False)
    user2_id:Mapped[UUID]=mapped_column(ForeignKey("users.id"),nullable=False)
    status:Mapped[ConversationStatus]=mapped_column(SQLEnum(ConversationStatus),nullable=False,default=ConversationStatus.ACTIVE_ANONYMOUS)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))
    Messages=relationship("Message",back_populates="Conversation",cascade="all, delete-orphan")
    User1=relationship("User",foreign_keys=[user1_id],back_populates="conversations_as_user1")
    User2=relationship("User",foreign_keys=[user2_id],back_populates="conversations_as_user2")