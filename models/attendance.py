from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    student_id = Column(String, ForeignKey('students.student_id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    room = Column(String, nullable=False)

    # Many to one relationship
    student = relationship("Student", back_populates="attendances")
