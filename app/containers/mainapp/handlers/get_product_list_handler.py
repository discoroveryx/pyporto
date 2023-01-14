from typing import List, Type

from core.parents.handlers import Handler

from containers.mainapp.entities.product_entity import ProductEntity
from containers.mainapp.repositories.product_repository import ProductRepository


class GetProductListHandler(Handler):
    def __init__(self, repository: Type[ProductRepository]) -> None:
        self.repository: ProductRepository = repository()

    def run(self, sort_by: str) -> List[ProductEntity]:
        return self.repository.fetch_all_products_with_sorting_by(sort_by)
