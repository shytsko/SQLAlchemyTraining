from typing import AsyncGenerator

from src.settings import settings
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    url=settings.database_url,
    echo=True
)

session_factory = async_sessionmaker(engine, autoflush=False, autocommit=False, expire_on_commit=False, )


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session


class Base(DeclarativeBase):
    pass


# async def create_all():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
