from app.models.users import Users
from app.repository.BaseRepo import BaseRepo


class UsersRepository(BaseRepo[Users]):
    model = Users