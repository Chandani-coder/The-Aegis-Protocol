from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.course import Course, Enrollment
from app.models.user import User
from app.schemas.course import CourseCreate
from app.api.deps import get_db, require_role

router = APIRouter()


@router.post("/")
def create_course(
    data: CourseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(require_role("faculty"))
):
    course = Course(
        code=data.code,
        name=data.name,
        faculty_id=user.id
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return {"success": True, "data": {"id": course.id}}


@router.post("/{course_id}/enroll")
def enroll(
    course_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(require_role("student"))
):
    enrollment = Enrollment(
        student_id=user.id,
        course_id=course_id
    )

    db.add(enrollment)
    db.commit()

    return {"success": True}
