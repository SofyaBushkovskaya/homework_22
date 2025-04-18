from django.core.cache import cache

from catalog.models import Product, Category

from config.settings import CACHES_ENABLED

def get_products_from_cache():
    """Получает данные по продуктам из кеша, если кеш пуст, получает данные из базы данных."""
    if not CACHES_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_products_by_category_from_cache(category_id):
    """Получает данные по продуктам в указанной категории из кеша, если кеш пуст, получает данные из базы данных."""
    if not CACHES_ENABLED:
        return Category.objects.filter(category_id=category_id)

    key = f"products_list_category_{category_id}"
    products = cache.get(key)

    if products is not None:
        return products

    products = Category.objects.filter(category_id=category_id)
    cache.set(key, products)
    return products
