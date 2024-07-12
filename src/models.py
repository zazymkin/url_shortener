from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(Text, nullable=False)
    short_url = Column(String(5), unique=True, index=True)
    click_count = Column(Integer, default=0)
