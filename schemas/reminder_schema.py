from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReminderCreate(BaseModel):
    user_id: int
    text: str
    time: datetime
    repeat: Optional[str] = None  # مثل 'daily', 'weekly'

class ReminderOut(BaseModel):
    id: int
    user_id: int
    text: str
    time: datetime
    repeat: Optional[str]
    sent: bool
