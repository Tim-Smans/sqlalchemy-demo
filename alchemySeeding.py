from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models.attendance import Attendance, Base as AttendanceBase
from models.student import Student, Base as StudentBase


engine = create_engine(
    "postgresql+pg8000://postgres:postgresPassword@localhost:5432/postgres"
)



# Creating the tables
AttendanceBase.metadata.create_all(engine)
StudentBase.metadata.create_all(engine)


# Creating Session
Session = sessionmaker(bind=engine)
session = Session()

# Adding a new student to db
new_student = Student(student_id="12345", name="Alice")

session.add(new_student)
session.commit()

# Adding an attendance to the db, with a relation to student
new_record = Attendance(
    student_id="12345",
    timestamp=datetime.now(),
    room="Room 101"
)

# Add the record to the session and commit it.
session.add(new_record)
session.commit()

print("Added attendance!")