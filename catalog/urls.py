from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path("", base, name="base"),
    path("contacts/", contacts, name="contacts")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)