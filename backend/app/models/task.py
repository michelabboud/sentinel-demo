import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(SQLEnum("todo", "in_progress", "done", name="status_enum"), default="todo")
    priority = Column(SQLEnum("low", "medium", "high", "critical", name="priority_enum"), default="medium")
    assignee_id = Column(String, ForeignKey("users.id"), nullable=True)
    group_id = Column(String, ForeignKey("groups.id"), nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    assignee = relationship("User", back_populates="tasks")
    group = relationship("Group", back_populates="tasks")
