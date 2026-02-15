from pydantic import BaseModel


class CourseCreate(BaseModel):
    code: str
    name: str
