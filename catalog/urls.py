from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", base, name="base"),
    path("contacts/", contacts, name="contacts")
]