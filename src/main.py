import asyncio
from src.database import session_factory
from models import FirstModel


async def main():
    # await create_all()
    data1 = FirstModel(data="data1")
    data2 = FirstModel(data="data2")

    async with session_factory() as session:
        session.add_all((data1, data2))
        await session.commit()


if __name__ == '__main__':
    asyncio.run(main())
