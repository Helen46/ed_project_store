from django.core.management import BaseCommand
import json

from django.db import connection

from catalog.models import Category, Product
from config.settings import CATALOG_DATA


class Command(BaseCommand):
    with connection.cursor() as cursor:
        cursor.execute(f"TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")
    with connection.cursor() as cursor:
        cursor.execute(f"TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE;")

    @staticmethod
    def json_read_categories():
        with open(CATALOG_DATA, encoding="utf-8") as file:
            catalog = json.load(file)
            return [item for item in catalog if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        with open(CATALOG_DATA, encoding="utf-8") as file:
            catalog = json.load(file)
            return [item for item in catalog if item["model"] == "catalog.products"]

    def handle(self, *args, **options):
        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    id=category["pk"],
                    name=category["fields"]["name"],
                )
            )
        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    id=product["pk"],
                    name=product["fields"]["name"],
                    price=product["fields"]["price"],
                    category=Category.objects.get(pk=product["fields"]["category"]),
                )
            )
        Product.objects.bulk_create(product_for_create)
