from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey,CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class ConversationStatus(Enum):
    ACTIVE_ANONYMOUS="active_anonymous"
    REVEAL_PENDING="reveal_pending"
    ACTIVE_REVEALED="active_revealed"

class Conversation(Base):
    __tablename__="conversations"
    __table_args__=(
        CheckConstraint("used1_id <> used2_id", name="check_used1_used2_different"),
    )
    id:Mapped[UUID]=mapped_column(primary_key=True, default=uuid4)
    used1_id:Mapped[UUID]=mapped_column(ForeignKey("users.id"),nullable=False)
    used2_id:Mapped[UUID]=mapped_column(ForeignKey("users.id"),nullable=False)
    status:Mapped[ConversationStatus]=mapped_column(SQLEnum(ConversationStatus),nullable=False,default=ConversationStatus.ACTIVE_ANONYMOUS)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))