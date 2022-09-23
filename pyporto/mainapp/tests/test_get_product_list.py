from rest_framework import status
from rest_framework.test import APITestCase

from mainapp.repositories.product_repository import ProductRepository
from mainapp.serializers import ProductListSerializer


class GetProductListTests(APITestCase):
    def test_get_product_list(self):
        """
        Get product list.
        """

        url = "/product-list/"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

        serializer = ProductListSerializer(
            ProductRepository().fetch_all_products_with_sorting_by("name"),
            many=True,
        )

        self.assertEqual(response.data["results"], serializer.data)
