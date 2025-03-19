from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import Base  # Import the shared Base

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    
    attendances = relationship("Attendance", back_populates="student")
