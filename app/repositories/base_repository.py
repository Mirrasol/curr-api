from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from sqlalchemy import select, insert


class AbstractRepository(ABC):
    @abstractmethod
    def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    def get_one_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def get_one_by_name(self, name: str):
        raise NotImplementedError


class AlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: Session):
        self.session = session

    def add_one(self, data: dict):
        query = insert(self.model).values(**data).returning(self.model)
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar_one()

    def get_one_by_id(self, id: int):
        query = select(self.model).where(self.model.id == id)
        result = self.session.execute(query)
        return result.scalar_one()

    def get_one_by_name(self, name: str):
        query = select(self.model).where(self.model.username == name)
        result = self.session.execute(query)
        return result.scalar_one()
