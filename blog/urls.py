from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView

app_name = BlogConfig.name

urlpatterns = [
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("", BlogListView.as_view(), name="blog_list"),
    # path("view/<int:pk>", BlogUpdateView.as_view(), name="blog_view"),
    # path("update/<int:pk>", BlogUpdateView.as_view(), name="blog_update"),
    # path("update/<int:pk>", BlogDeleteView.as_view(), name="blog_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
