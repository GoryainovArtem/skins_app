from typing import Annotated
import enum

from sqlalchemy import ForeignKey, CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True,
                                     nullable=False)]

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }


class ItemType(enum.Enum):
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


class WearCondition(enum.Enum):
    fn = "Прямо с завода"
    mw = "Немного поношенный"
    ft = "После полевых испытаний"
    ww = "Поношенный"
    bs = "Закаленный в боях"


class ItemORM(Base):
    __tablename__ = "items"
    id_item: Mapped[intpk]
    item_name: Mapped[str] = mapped_column(unique=True)
    item_type: Mapped[ItemType]


class CaseORM(Base):
    __tablename__ = "cases"
    id_case: Mapped[intpk]
    case_name: Mapped[str] = mapped_column(unique=True)
    case_image_url: Mapped[str] = mapped_column(unique=True) # Нужна URL валидация


class RarityORM(Base):
    __tablename__ = "rarities"
    id_rarity: Mapped[intpk]
    rarity_name: Mapped[str] = mapped_column(unique=True)
    rarity_color: Mapped[str] = mapped_column() # Валидация на длину в 7 символов и 1 символ #


class SkinORM(Base):
    __tablename__ = "skins"
    id_skin: Mapped[intpk]
    rarity_name: Mapped[int] = mapped_column(ForeignKey("rarities.id_rarity",
                                                        ondelete="CASCADE")
                                             )
    id_item: Mapped[int] = mapped_column(ForeignKey("items.id_item",
                                                      ondelete="CASCADE")
                                         )
    id_case: Mapped[int] = mapped_column(ForeignKey("cases.id_case", ondelete="CASCADE"))
    skin_name: Mapped[str] = mapped_column(unique=True)
    skin_image_url: Mapped[str] = mapped_column()


# class StoreSkinORM(Base):
#     __tablename__ = "store_skins"
#
#     id_store_skin = ...
#     id_skin = ...
#     id_wear_condition = ...


# class Customer(Base):
#     ...
