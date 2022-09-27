from abc import ABC
from dataclasses import dataclass


@dataclass(init=True, eq=True, frozen=True)
class DTO(ABC):
    """
    Data Transfer Object (DTO)

    DTO is used for data transport between layers.
    DTO is an immutable object, it does not have ID's, it does not have any logic.

    Controller/View -> DTO -> Action
    """
    ...
