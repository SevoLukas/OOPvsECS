from typing import Dict, Any
import enum

from ECS.entities2 import EntityType


class ComponentType(enum.Enum):
    price = "price"


class ComponentRegistry:
    def __init__(self):
        self._registry: Dict[ComponentType, object] = {}

    def register_component(self, key: ComponentType, component: Any) -> None:
        """
        Registers a shared component instance under a specific key (enum member).
        """
        self._registry[key] = component

    def get_component(self, key: ComponentType) -> Any:
        """
        Returns the component instance registered under the given key,
        or None if not found.
        """
        return self._registry.get(key)


class EntityRegistry:
    def __init__(self):
        self._next_id = 0
        self._entities: dict[int, object] = {}

    def create_entity(self, entity_type: EntityType) -> object:
        """
        Creates an entity of the given class with a unique entity_id.
        Additional keyword arguments are passed to the entity constructor.
        """
        entity = entity_type.value(entity_id=self._next_id)
        self._entities[self._next_id] = entity
        self._next_id += 1
        return entity

    def get_entity(self, entity_id: int) -> object:
        """
        Retrieves and returns the entity by its entity_id.
        """
        return self._entities.get(entity_id)

    def remove_entity(self, entity_id: int) -> None:
        """
        Removes the entity from the registry.
        """
        if entity_id in self._entities:
            del self._entities[entity_id]
