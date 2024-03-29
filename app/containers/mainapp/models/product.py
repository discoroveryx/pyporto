from django.db import models

from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    @staticmethod
    def objects_all_order_by(*args, **kwargs):
        return Product._get_all_fake_fixtures()

    @staticmethod
    def _get_all_fake_fixtures():
        return [
            {"pk": 1, "name": "Product 1", "price": 100.00},
            {"pk": 2, "name": "Product 2", "price": 200.00},
        ]

    class Meta:
        db_table = "product"
