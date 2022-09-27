from abc import ABC
from dataclasses import dataclass


@dataclass(init=True, eq=True, frozen=True)
class Value(ABC):
    """
    ValueObject

    ValueObject just hold data.
    ValueObject is an immutable object, it does not have ID's.

    Action <-> Task
    """
    ...
