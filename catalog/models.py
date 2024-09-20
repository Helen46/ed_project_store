from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="products/photo",
        verbose_name="Фото",
        help_text="Загрузите фото товара",
        **NULLABLE,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name="products",
        **NULLABLE,
    )
    price = models.FloatField(
        verbose_name="Цена продукта",
        help_text="Введите цену продукта",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания (записи в БД)",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения (записи в БД)",
        auto_now=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name", "price", "created_at", "updated_at"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


# продукт,
# номер версии,
# название версии,
# признак текущей версии.
class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="product_version",
        on_delete=models.SET_NULL,
        verbose_name="Продукт",
        **NULLABLE
    )
    number = models.CharField(
        verbose_name="Номер версии",
        help_text="Введите номер верси",
        **NULLABLE
    )
    version_name = models.CharField(
        max_length=150,
        verbose_name="Название версии",
        help_text="Введите название верси",
        **NULLABLE
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Версия активна",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продукта"
        ordering = ["version_name"]

    def __str__(self):
        return self.version_name
