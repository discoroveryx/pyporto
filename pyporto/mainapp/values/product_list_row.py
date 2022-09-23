from dataclasses import dataclass

from core.parents.values.value import Value


@dataclass(init=True, eq=True, frozen=True)
class ProductListRowValue(Value):
    product_id: int
    name: str
    price: float
