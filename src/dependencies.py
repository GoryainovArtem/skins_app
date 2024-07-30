from src.skins.services.skin_service import SkinService
from src.skins.repositories.skin_repository import SkinRepository


def skins_service():
    return SkinService(SkinRepository)