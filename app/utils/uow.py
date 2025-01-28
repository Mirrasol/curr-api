from abc import ABC, abstractmethod
from app.db.database import session_maker
from app.repositories.users_repository import UserRepository


class IUnitOfWork(ABC):
    user: UserRepository

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *args):
        pass

    @abstractmethod
    def rollback(self):
        pass


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = session_maker

    def __enter__(self):
        self.session = self.session_factory()
        self.user = UserRepository(self.session)

    def __exit__(self, *args):
        self.rollback()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
