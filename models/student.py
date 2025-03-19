from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    
    # One-to-many relationship
    attendances = relationship("Attendance", back_populates="student")


