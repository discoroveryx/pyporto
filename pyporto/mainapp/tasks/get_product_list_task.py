from typing import List

from core.parents.tasks.task import Task

from mainapp.entities.product_entity import ProductEntity
from mainapp.repositories.product_repository import ProductRepository


class GetProductListTask(Task):
    def __init__(self, repository: ProductRepository) -> None:
        self.repository: ProductRepository = repository()

    def run(self, sort_by: str) -> List[ProductEntity]:
        return self.repository.fetch_all_products_with_sorting_by(sort_by)
