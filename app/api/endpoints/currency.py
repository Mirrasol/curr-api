from fastapi import APIRouter
from app.api.schemas.currency import Currencies

currency_router = APIRouter(
    prefix='/currency',
    tags=['Currency'],
)


@currency_router.get('/list')
def show_currencies_list(user):
    pass


@currency_router.post('/exchange')
def exchange_currency(currencies: Currencies, user):
    pass
