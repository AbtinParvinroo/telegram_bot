from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(String, nullable=False)
    remind_at = Column(DateTime, nullable=False)
    repeat = Column(String, default="none")  # none, daily, weekly, monthly
    is_active = Column(Boolean, default=True)

    user = relationship("User", backref="reminders")

    def __repr__(self):
        return f"<Reminder id={self.id} user_id={self.user_id} remind_at={self.remind_at}>"
