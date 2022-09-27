from rest_framework.views import APIView

from containers.mainapp.actions.get_product_list_action import GetProductListAction
from containers.mainapp.dto.product_list_dto import ProductListDTO
from containers.mainapp.paginations import ProductListPagination
from containers.mainapp.serializers import ProductListSerializer


class ProductListView(APIView):
    """
    Get list of products.
    """

    def get(self, request, *args, **kwargs):
        params = ProductListDTO(
            user_is_authenticated=request.user.id,
        )

        product_list = GetProductListAction().run(params)

        serializer = ProductListSerializer(product_list, many=True)

        paginator = ProductListPagination()

        paginated_queryset = paginator.paginate_queryset(serializer.data, request)

        paginated_response = paginator.get_paginated_response(paginated_queryset)

        return paginated_response
