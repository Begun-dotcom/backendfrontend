from src.dao.basedao import BaseDao
from src.dao.models import Order, User


class OrderDao(BaseDao):
    model = Order


class UserDao(BaseDao):
    model = User