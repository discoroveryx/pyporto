from django.urls import include, path

urlpatterns = [
    path("", include("mainapp.api.urls.product_list_v1")),
]
