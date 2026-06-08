from typing import TypeVar, Generic
from loguru import logger
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.base import Base

T = TypeVar("T", bound=Base)


class BaseDao(Generic[T]):
    model: type[T]

    def __init__(self, session: AsyncSession):
        self._session = session


    async def add(self, filters: BaseModel):
        try:
            filter_dict = filters.model_dump(exclude_unset=True)
            self._session.add(self.model(**filter_dict))
            await self._session.commit()
            logger.info(f"Данные в {self.model.__name__} добавлены успешно")
            return True
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка SQLAlchemy в {self.model.__name__}: {e}")
            raise RuntimeError(f"Ошибка при работе с базой данных: {e}")
        except Exception as e:
            logger.error(f"Ошибка добавления в таблицу {self.model}: {e}")
            return False

    async def get_others(self, filters: BaseModel | None = None):
        try:
            filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
            query = select(self.model).filter_by(**filter_dict)
            result = await self._session.execute(query)
            logger.info(f"Данные из {self.model.__name__} с параметрами {filters} получены успешно")
            return result.scalars().all()
        except Exception as e:
            logger.error(f"Ошибка получения данных из {self.model.__name__}: {e}")
            return None