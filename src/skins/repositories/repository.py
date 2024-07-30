from abc import ABC, abstractmethod

from sqlalchemy import select

from src.database import async_session_factory


class AbstractRepository(ABC):

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_all(self):
        async with async_session_factory() as session:
            query = select(self.model)
            data = await session.execute(query)
            return data.scalars().all()
