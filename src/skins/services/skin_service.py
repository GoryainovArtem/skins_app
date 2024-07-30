from src.skins.repositories.repository import AbstractRepository


class SkinService:

    def __init__(self, repo: AbstractRepository):
        self.skin_repo: AbstractRepository = repo()

    async def get_all_skins(self):
        return await self.skin_repo.get_all()

    async def get_skin(self, skin_name: str):
        return await self.skin_repo.get_skin(skin_name)

    async def add_skin(self):
        ...