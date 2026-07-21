import uuid
from dataclasses import dataclass, field
from .interfaces import Cloneable

@dataclass
class Entity(Cloneable):
    """Base entity model representing a uniquely identifiable object."""

    id: str = field(default_factory = lambda: str(uuid.uuid4()))
    name: str = "Unnamed Entity"

    def clone(self) -> 'Entity':
        """Creates a clone with a new unique ID."""
        return Entity(
            id = str(uuid.uuid4()),
            name=f"{self.name} (Copy)"
        )