from abc import ABC
from dataclasses import dataclass


@dataclass(init=True, eq=True, frozen=True)
class Entity(ABC):
    """
    Data Access Object (DAO, Entity, Transporter)

    To abstract access to a data source (DB, ORM).
    DAO is an immutable object and can has ID's.

    BusinessObject <-> DAO <-> Repository <-> DataSource/ORM
    """
    ...
