from pydantic import BaseModel


class Currency(BaseModel):
    """Pydantic model for currencies"""
    from_currency: str
    to_currency: str
    amount: float = 1
