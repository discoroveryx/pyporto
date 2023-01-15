from typing import Any, List

from core.parents.repositories.repository import Repository
from django.db.models import Avg, F, Max, Window

from containers.mainapp.entities.product_max_price_entity import ProductWithMaxPriceInCategoryEntity
from containers.mainapp.models.product import Product


class ProductAggregationRepository(Repository):
    def model(self) -> str:
        return str(Product.__class__.__name__)

    def fetch_all_product_with_max_price_in_category(self) -> List[ProductWithMaxPriceInCategoryEntity]:
        products = Product.objects.all().annotate(
            max_price_in_category=Window(
                expression=Max("price"),
                partition_by=[F('category')],
                order_by='category__pk',
            )
        )

        return list(map(self._get_row, products))

    def _get_row(self, row: Product) -> ProductWithMaxPriceInCategoryEntity:
        return ProductWithMaxPriceInCategoryEntity(
            product_id=row.pk,
            name=row.name,
            price=row.price,
            max_price_in_category=row.max_price_in_category,
            category_name=row.category.name,
        )