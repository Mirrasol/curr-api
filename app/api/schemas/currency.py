from pydantic import BaseModel


class Currency(BaseModel):
    from_currency: str
    to_currency: str
    amount: float = 1
