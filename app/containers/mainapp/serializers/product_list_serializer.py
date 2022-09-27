from rest_framework import serializers


class ProductListSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=128)
    name = serializers.CharField(max_length=128)
    price = serializers.FloatField()
