from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.db.base import Base


class Grievance(Base):
    __tablename__ = "grievances"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(String, default="submitted")
    is_anonymous = Column(Boolean, default=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
