from typing import Any, List

from core.parents.repositories.repository import Repository

from mainapp.entities.product_entity import ProductEntity
from mainapp.models.product import Product


class ProductRepository(Repository):
    def model(self) -> str:
        return str(Product.__class__.__name__)

    def fetch_all_products_with_sorting_by(self, sort_by: str) -> List[ProductEntity]:
        products = self._fetch_all_products_with_sorting_by(sort_by)

        return list(map(self._get_row, products))

    def _fetch_all_products_with_sorting_by(self, sort_by: str) -> Any:
        return Product.objects_all_order_by(sort_by)

    def _get_row(self, row: dict) -> ProductEntity:
        return ProductEntity(
            product_id=row["pk"],
            name=row["name"],
            price=row["price"],
        )
