from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .base import Base

class MusicList(Base):
    __tablename__ = "music_list"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime)
    tags = Column(String)  # comma-separated tags
    is_public = Column(Boolean, default=True)

    def __repr__(self):
        return f"<MusicList id={self.id} title={self.title}>"
