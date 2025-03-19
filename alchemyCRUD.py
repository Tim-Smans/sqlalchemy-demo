from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.student import Student
from models.attendance import Attendance

engine = create_engine(
    "postgresql+pg8000://postgres:postgresPassword@localhost:5432/postgres"
)


Session = sessionmaker(bind=engine)
session = Session()

# CREATE

def create_student(student_id: str, name: str):
    new_record = Student(
    student_id=student_id,
    name=name
    )   

    # Add the record to the session and commit it.
    session.add(new_record)
    session.commit()


def create_attendance(student_id: str, room: str):
    new_record = Attendance(
    student_id=student_id,
    timestamp=datetime.now(),
    room=room
    )   

    # Add the record to the session and commit it.
    session.add(new_record)
    session.commit()
        
# READ

def get_all_students():
    students = session.query(Student)
    for student in students.all():
        print(student.student_id, " - ",student.name)

def get_all_students_with_attendance():
    students = session.query(Student)
    for student in students.all():
        print(f"Attendance for {student.name}")
        for attendance in student.attendances:
            print("- Id:", attendance.id , "Timestamp: ", attendance.timestamp, "Room: ", attendance.room)
    
    
# UPDATE
def update_student(student_id: str, newStudent: Student):
    og_student = session.query(Student).filter_by(student_id=student_id).first()
    
    if(student_id != newStudent.student_id):
        print("Student id's do not match.")
        return
    
    if og_student:
        for key, value in vars(newStudent).items():
            if key.startswith('_'):
                continue  # Skip SQLAlchemy internals
            if hasattr(og_student, key):
                setattr(og_student, key, value)
                
        session.commit()
        print("Student updated!")
    else:
        print("Student not found.")
        

def delete_student(student_id: str):
    student = session.query(Student).filter_by(student_id=student_id).first()

    if(student):
        session.delete(student)
        session.commit
        print("Deleted student")
    else:
        print("Student does not exist")

get_all_students()