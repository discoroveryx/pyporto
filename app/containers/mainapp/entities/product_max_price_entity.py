from dataclasses import dataclass

from core.parents.entities import Entity

from containers.mainapp.types.product_id_type import ProductId


@dataclass(init=True, eq=True, frozen=True)
class ProductWithMaxPriceInCategoryEntity(Entity):
    product_id: ProductId
    name: str
    price: float
    max_price_in_category: float
    category_name: str
