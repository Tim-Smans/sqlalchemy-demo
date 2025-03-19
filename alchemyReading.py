from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.student import Student
from models.attendance import Attendance

engine = create_engine(
    "postgresql+pg8000://postgres:postgresPassword@localhost:5432/postgres"
)


Session = sessionmaker(bind=engine)
session = Session()

# Query: Getting al attendances from a specific student.
student = session.query(Student).filter_by(student_id="12345").first()
for attendance in student.attendances:
    print("- Id:", attendance.id , "Timestamp: ", attendance.timestamp, "Room: ", attendance.room)