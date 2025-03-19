from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Import same Base

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    student_id = Column(String, ForeignKey('students.student_id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    room = Column(String, nullable=False)

    student = relationship("Student", back_populates="attendances")
