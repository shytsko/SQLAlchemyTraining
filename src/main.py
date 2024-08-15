import asyncio
from src.database import session_factory
from models import Department, Workplace, WorkplaceType
from sqlalchemy import select, update


async def fill_db():
    async with session_factory() as session:
        department1 = Department(name="Руководство")
        department2 = Department(name="Технический отдел")
        session.add_all((department1, department2))
        await session.flush()

        workplace1 = Workplace(
            name="Директор",
            workplace_type=WorkplaceType.SUPERVISOR,
            department=department1
        )

        workplace2 = Workplace(
            name="Заместитель директора",
            workplace_type=WorkplaceType.SUPERVISOR,
            department=department1
        )
        workplace3 = Workplace(
            name="Главный инженер",
            workplace_type=WorkplaceType.SUPERVISOR,
            department=department1
        )

        workplace4 = Workplace(
            name="Начальник отдела",
            workplace_type=WorkplaceType.SUPERVISOR,
            department=department2
        )
        workplace5 = Workplace(
            name="Технолог",
            workplace_type=WorkplaceType.SPECIALIST,
            department=department2
        )
        workplace6 = Workplace(
            name="Контролер качества",
            workplace_type=WorkplaceType.WORKER,
            quantity=3,
            department=department2
        )

        session.add_all((workplace1, workplace2, workplace3, workplace4, workplace5, workplace6))
        await session.commit()


async def get_workplace(workplace_id: int) -> Workplace:
    async with session_factory() as session:
        query = select(Workplace).filter_by(id=workplace_id)
        result = await session.execute(query)
        workplace = result.scalar()
        return workplace


async def main():
    # await fill_db()
    workplace = await get_workplace(2)
    workplace.name = "Первый заместитель директора"
    async with session_factory() as session:
        session.add(workplace)
        await session.commit()
    print(workplace.workplace_type)


if __name__ == '__main__':
    asyncio.run(main())
