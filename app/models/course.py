from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    faculty_id = Column(Integer, ForeignKey("users.id"))


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
