from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class RevealRequestStatus(Enum):
    PENDING="pending"
    ACCEPTED="accepted"
    REJECTED="rejected"
    CANCELLED="cancelled"
class RevealRequest(Base):
    __tablename__="reveal_requests"
    id:Mapped[UUID]=mapped_column(primary_key=True, default=uuid4)
    conversation_id:Mapped[UUID]=mapped_column(ForeignKey("conversations.id"),nullable=False)
    requested_by:Mapped[UUID]=mapped_column(ForeignKey("users.id"),nullable=False)
    status:Mapped[RevealRequestStatus]=mapped_column(SQLEnum(RevealRequestStatus),nullable=False,default=RevealRequestStatus.PENDING)
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))
    responded_at:Mapped[datetime|None]=mapped_column(DateTime(timezone=True),nullable=True)