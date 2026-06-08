from fastapi import Depends

from src.config import setting

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import Annotated, AsyncGenerator
# URL = setting.LOCAL_DB
URL = setting.get_url

async_engine = create_async_engine(url=URL,echo=True,future=True)

async_session_maker = async_sessionmaker(bind=async_engine, class_=AsyncSession)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_db)]