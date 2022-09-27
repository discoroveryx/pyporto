from typing import List

from core.parents.actions.action import Action

from containers.mainapp.constants import SORT_BY_DEFAULT
from containers.mainapp.dto.product_list_dto import ProductListDTO
from containers.mainapp.repositories.product_repository import ProductRepository
from containers.mainapp.tasks.get_product_list_task import GetProductListTask
from containers.mainapp.values.product_list_row import ProductListRowValue


class GetProductListAction(Action):
    def run(self, params: ProductListDTO) -> List[ProductListRowValue]:
        if params.user_is_authenticated:
            products = GetProductListTask(ProductRepository).run(sort_by='product_id')
        else:
            products = GetProductListTask(ProductRepository).run(sort_by=SORT_BY_DEFAULT)

        return products
