from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.base import Base


class Order(Base):
    phone: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(500))
    status: Mapped[str] = mapped_column(String(20), default="pending")

    def __repr__(self) -> str:
        return f"Order(phone={self.phone}, description={self.description}, status={self.status})"

class User(Base):
    login: Mapped[str]
    password: Mapped[str]
    role: Mapped[str]

    def __repr__(self) -> str:
        return f"User(login={self.login}, role={self.role})"