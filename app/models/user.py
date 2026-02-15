
from sqlalchemy import Column, Integer, String, Enum
from app.db.base import Base
import enum


class RoleEnum(str, enum.Enum):
    student = "student"
    faculty = "faculty"
    authority = "authority"
    admin = "admin"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
