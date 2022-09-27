from dataclasses import dataclass

from core.parents.dto.dto import DTO


@dataclass(init=True, eq=True, frozen=True)
class ProductListDTO(DTO):
    user_is_authenticated: bool
