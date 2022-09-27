"""
Get all products [ver. 1].
"""

from django.urls import path

from containers.mainapp.api.views.product_list_view import ProductListView

urlpatterns = [
    path('product-list/', ProductListView.as_view()),
]
