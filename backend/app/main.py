from typing import Annotated
import enum

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True,
                                     nullable=False)]


class Base(DeclarativeBase):
    ...


class WeaponType(enum.Enum):
    rifle = "Винтовка"
    sniper_rifle = "Снайперская винтовка"
    pistol = "Пистолет"
    knife = "Нож"
    machine_pistol = "Пистолет-пулемет"
    machinegun = "Пулемет"
    shotgun = "Дробовик"
    gloves = "Перчатки"
    sticker = "Наклейка"
    case = "Кейс"


class WeaponORM(Base):
    __tablename__ = "weapons"
    id_weapon: Mapped[int] = mapped_column(primary_key=True)
    name_weapon: Mapped[str] = mapped_column(unique=True)
    type_weapon: Mapped[WeaponType]


class Rarity(Base):
    __tablename__ = "rarities"
    id_rarity: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,
                                           nullable=False)
    name_rarity: Mapped[str] = mapped_column(unique=True)
    color_rarity: Mapped[str] = mapped_column()


class SkinORM(Base):
    __tablename__ = "skins"
    id_skin: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,
                                         nullable=False)
    name_skin: Mapped[str] = mapped_column(unique=True)
    id_rarity: Mapped[int] = mapped_column(ForeignKey("rarities.id_rarity",
                                                      ondelete="CASCADE")
                                           )
    id_weapon: Mapped[int] = mapped_column(ForeignKey("weapons.id_weapon",
                                                      ondelete="CASCADE")
                                           )

