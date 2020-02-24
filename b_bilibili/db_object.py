from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Integer,Column,String


class Video(Base):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    creation_time = Column(Integer)
    av_number = Column(String)
    title = Column(String)
    cover_local = Column(String)
    video = Column(String)
    video_download_url = Column(String)