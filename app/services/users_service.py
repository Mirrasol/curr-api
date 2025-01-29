from app.api.schemas.users import UserCreate, UserFromDB
from app.utils.uow import IUnitOfWork
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_token
from app.core.exception_handlers import InvalidCredentialsException, UserExistsException


class UserService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def add_user(self, user_data: UserCreate):
        user_dict = user_data.model_dump()
        with self.uow:
            try:
                user_from_db = self.uow.user.add_one(user_dict)
            except:
                raise UserExistsException
            user_result = UserFromDB.model_validate(user_from_db)
            self.uow.commit()
            return user_result

    def get_user_by_name(self, username: str):
        with self.uow:
            user_result = self.uow.user.get_one_by_name(username)
            if user_result is None:
                raise InvalidCredentialsException
            return user_result

    def get_jwt_token(self, data: OAuth2PasswordRequestForm):
        with self.uow:
            user_from_db = self.uow.user.get_one_by_name(data.username)
            if user_from_db is None or user_from_db.password != data.password:
                raise InvalidCredentialsException
            current_token = create_token({"sub": data.username})
            return current_token
