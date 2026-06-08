from src.dao.basedao import BaseDao
from src.dao.models import Order


class OrderDao(BaseDao):
    model = Order