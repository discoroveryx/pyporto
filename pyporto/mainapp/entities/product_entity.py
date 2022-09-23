from dataclasses import dataclass

from core.parents.entities.entity import Entity

from mainapp.types.product_id_type import ProductId


@dataclass(init=True, eq=True, frozen=True)
class ProductEntity(Entity):
    product_id: ProductId
    name: str
    price: float
