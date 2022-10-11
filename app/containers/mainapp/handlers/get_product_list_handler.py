from typing import List

from core.parents.handlers.handler import Handler

from containers.mainapp.entities.product_entity import ProductEntity
from containers.mainapp.repositories.product_repository import ProductRepository


class GetProductListHandler(Handler):
    def __init__(self, repository: ProductRepository) -> None:
        self.repository: ProductRepository = repository()

    def run(self, sort_by: str) -> List[ProductEntity]:
        return self.repository.fetch_all_products_with_sorting_by(sort_by)
