from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    telegram_id: int
    username: Optional[str]
    language: Optional[str] = "fa"
    theme: Optional[str] = "default"

class UserOut(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str]
    language: str
    theme: str
