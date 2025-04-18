from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    language = Column(String, default="en")
    theme = Column(String, default="light")
    notifications_enabled = Column(Boolean, default=True)
    content_filter = Column(Boolean, default=True)
    message_template = Column(String, default="{message}")

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"
