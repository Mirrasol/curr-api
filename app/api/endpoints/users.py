from fastapi import APIRouter

auth_router = APIRouter(
    prefix='/auth',
    tags=['Authenticate'],
)


@auth_router.post('/register/')
def register_user():
    pass


@auth_router.post('/login/')
def login():
    pass
