from pydantic import BaseModel


class GrievanceCreate(BaseModel):
    title: str
    description: str
    is_anonymous: bool = False


class GrievanceStatusUpdate(BaseModel):
    status: str
