from app.db.models import User
from app.repositories.base_repository import AlchemyRepository


class UserRepository(AlchemyRepository):
    """Combine SQLAlchemy Repository with User model"""
    model = User
