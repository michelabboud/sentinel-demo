from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GroupCreate(BaseModel):
    name: str
    description: Optional[str] = None


class GroupRead(BaseModel):
    id: str
    name: str
    description: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class GroupUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
