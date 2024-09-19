from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, contacts,
                           ProductCreateView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("catalog/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", contacts, name="contacts"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    # path("delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"),
]
