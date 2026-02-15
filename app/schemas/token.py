from pydantic import BaseModel


class TokenResponse(BaseModel):
    success: bool
    access_token: str
