from app.api.schemas.users import UserCreate, UserFromDB
from app.utils.uow import IUnitOfWork
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_token
from app.core.hash import get_password_hash, verify_password
from sqlalchemy.exc import NoResultFound
from app.core.exception_handlers import InvalidCredentialsException, UserExistsException


class UserService:
    """A service to manage user routes"""
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def add_user(self, user_data: UserCreate):
        user_dict = user_data.model_dump()
        user_dict['password'] = get_password_hash(user_data.password)
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
            try:
                user_from_db = self.uow.user.get_one_by_name(data.username)
            except (NoResultFound):
                raise InvalidCredentialsException
            if not verify_password(password=data.password, hashed_password=user_from_db.password):
                raise InvalidCredentialsException
            current_token = create_token({"sub": data.username})
            return current_token
