from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content",)
    success_url = reverse_lazy("catalog:catalog_list")


class BlogListView(ListView):
    model = Blog
