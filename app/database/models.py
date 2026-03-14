from app.database.connection import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from datetime import datetime


class Moderator(Base):
    __tablename__ = "tbmoderator"

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String, nullable=False)

    assignments = relationship("Assignment", back_populates="moderator")

class Event(Base):
    __tablename__ = "tbevent"

    event_id = Column(Integer, primary_key=True, index=True)
    region = Column(String, nullable=False)
    payload = Column(JSONB, nullable=True)
    is_claim = Column(Boolean, default=False)

    assignments = relationship("Assignment", back_populates="event")

class Assignment(Base):
    __tablename__ = "tbassignment"

    id = Column(Integer, primary_key=True, index=True)

    event_id = Column(Integer, ForeignKey("tbevent.event_id"))
    moderator_id = Column(Integer, ForeignKey("tbmoderator.id"))

    dt_tm_claim = Column(DateTime, default=datetime.utcnow)
    dt_tm_expire = Column(DateTime)

    is_acknowledge = Column(Boolean, default=False)

    event = relationship("Event", back_populates="assignments")
    moderator = relationship("Moderator", back_populates="assignments")