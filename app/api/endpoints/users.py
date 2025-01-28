from fastapi import APIRouter, Depends
from app.services.users_service import UserService
from app.utils.uow import IUnitOfWork, UnitOfWork
from app.api.schemas.users import UserCreate, UserFromDB


auth_router = APIRouter(
    prefix='/auth',
    tags=['Authenticate'],
)


def get_user_service(uow: IUnitOfWork = Depends(UnitOfWork)) -> UserService:
    return UserService(uow)


@auth_router.post('/register/')
def register_user(user_data: UserCreate, user_service: UserService = Depends(get_user_service)):
    return user_service.add_user(user_data)


@auth_router.post('/login/')
def login():
    pass
