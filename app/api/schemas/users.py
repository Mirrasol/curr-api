from pydantic import BaseModel, ConfigDict
import datetime


class UserCreate(BaseModel):
    """Pydantic model for user registration"""
    model_config = ConfigDict(from_attributes=True)

    username: str
    password: str


class UserFromDB(UserCreate):
    """Pydantic model for a registered user"""
    id: int
    created_at: datetime.datetime
