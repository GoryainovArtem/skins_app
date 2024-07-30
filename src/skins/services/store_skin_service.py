from src.skins.repositories.repository import AbstractRepository


class StoreSkinService:
    def __init__(self, repo: AbstractRepository):
        self.repo = repo

    async def get_all_store_skins(self):
        return await self.repo().get_all()
