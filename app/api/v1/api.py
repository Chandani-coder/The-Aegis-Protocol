from fastapi import APIRouter
from app.api.v1.endpoints import auth, grievances, academics

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(grievances.router, prefix="/grievances", tags=["Grievances"])
api_router.include_router(academics.router, prefix="/academics", tags=["Academics"])
