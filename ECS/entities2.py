import enum
from dataclasses import dataclass


@dataclass
class BookProductEntity:
    entity_id: int

@dataclass
class MagazineProductEntity:
    entity_id: int


class EntityType(enum.Enum):
    book = BookProductEntity
    magazine = MagazineProductEntity
