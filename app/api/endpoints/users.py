from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.services.users_service import UserService
from app.utils.uow import IUnitOfWork, UnitOfWork
from app.api.schemas.users import UserCreate


auth_router = APIRouter(
    prefix='/auth',
    tags=['Authenticate'],
)


def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)


@auth_router.post('/register/')
def register_user(user_data: UserCreate, user_service: UserService = Depends(get_user_service)):
    """New user registration"""
    user_service.add_user(user_data)
    return {'message': 'User added successfully'}


@auth_router.post('/login/')
def login(user_data: Annotated[OAuth2PasswordRequestForm, Depends()], user_service: UserService = Depends(get_user_service)):
    """Login for registered users"""
    current_token = user_service.get_jwt_token(user_data)
    return {'access_token': current_token}
