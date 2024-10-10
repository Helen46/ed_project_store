from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает данные по активным продуктам из кэша, если кэш пуст получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.filter(is_published=True)
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.filter(is_published=True)
    cache.set(key, products)
    return products
