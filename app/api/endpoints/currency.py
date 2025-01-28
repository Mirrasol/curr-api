from fastapi import APIRouter
from app.api.schemas.currency import Currency
from app.utils.external_api import get_currencies_list, get_current_exchange_rates

currency_router = APIRouter(
    prefix='/currency',
    tags=['Currency'],
)


@currency_router.get('/list')
def show_currencies_list():
    currency_list = get_currencies_list()
    return currency_list


@currency_router.post('/exchange')
def exchange_currency(currencies: Currency):
    result = get_current_exchange_rates(currencies)
    return result
