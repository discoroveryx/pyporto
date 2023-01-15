from unittest import mock

from rest_framework.test import APITestCase

from containers.mainapp.entities.product_max_price_entity import ProductWithMaxPriceInCategoryEntity
from containers.mainapp.models.category import Category
from containers.mainapp.models.product import Product
from containers.mainapp.repositories.product_aggregation_repository import (
    ProductAggregationRepository,
)


class FetchProductListWithMaxPriceInCategoryTestCase(APITestCase):
    def setUp(self):
        category_1 = Category.objects.create(name="Category_1")
        category_2 = Category.objects.create(name="Category_2")

        Product.objects.create(name="Product_1", price=100, category=category_1)
        Product.objects.create(name="Product_2", price=200, category=category_1)
        Product.objects.create(name="Product_3", price=300, category=category_2)
        Product.objects.create(name="Product_4", price=400, category=category_2)

    def test_fetch_product_list_with_max_price_in_category(self):
        data = ProductAggregationRepository().fetch_all_product_with_max_price_in_category()

        expected_data = [
            ProductWithMaxPriceInCategoryEntity(
                product_id=mock.ANY,
                name="Product_1",
                price=100.0,
                max_price_in_category=200.0,
                category_name="Category_1",
            ),
            ProductWithMaxPriceInCategoryEntity(
                product_id=mock.ANY,
                name="Product_2",
                price=200.0,
                max_price_in_category=200.0,
                category_name="Category_1",
            ),
            ProductWithMaxPriceInCategoryEntity(
                product_id=mock.ANY,
                name="Product_3",
                price=300.0,
                max_price_in_category=400.0,
                category_name="Category_2",
            ),
            ProductWithMaxPriceInCategoryEntity(
                product_id=mock.ANY,
                name="Product_4",
                price=400.0,
                max_price_in_category=400.0,
                category_name="Category_2",
            ),
        ]

        self.assertCountEqual(data, expected_data)
