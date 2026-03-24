import uuid
from sqlalchemy import Column, String, Enum as SQLEnum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(SQLEnum("admin", "manager", "user", name="role_enum"), nullable=False, default="user")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, nullable=True)

    # Cascade delete: when a user is deleted, their tasks are also deleted
    tasks = relationship("Task", back_populates="assignee", cascade="all, delete-orphan")
    groups = relationship("Group", secondary="group_members", back_populates="members")
