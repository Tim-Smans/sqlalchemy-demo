from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models.attendance import Attendance, Base 


engine = create_engine(
    "postgresql+pg8000://postgres:postgresPassword@localhost:5432/postgres"
)



# Creating the tables
Base.metadata.create_all(engine)


# Creating Session
Session = sessionmaker(bind=engine)
session = Session()



# Adding a record to the table
new_record = Attendance(
    student_id="12345",
    timestamp=datetime.now(),
    room="Room 101"
)


# Add the record to the session and commit it.
session.add(new_record)
session.commit()

print("Added attendance!")