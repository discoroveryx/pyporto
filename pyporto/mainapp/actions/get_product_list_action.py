from typing import List

from core.parents.actions.action import Action

from mainapp.dto.product_list_dto import ProductListDTO
from mainapp.repositories.product_repository import ProductRepository
from mainapp.tasks.get_product_list_task import GetProductListTask
from mainapp.values.product_list_row import ProductListRowValue


class GetProductListAction(Action):
    def run(self, params: ProductListDTO) -> List[ProductListRowValue]:
        if params.user_is_authenticated:
            products = GetProductListTask(ProductRepository).run(sort_by="product_id")
        else:
            products = GetProductListTask(ProductRepository).run(sort_by="name")

        return products
