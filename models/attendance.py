from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    student_id = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    room = Column(String, nullable=False)



