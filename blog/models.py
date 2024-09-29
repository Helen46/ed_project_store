from django.db import models

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название"
    )
    content = models.TextField(verbose_name="Текст статьи", help_text="Введите текст")
    image = models.ImageField(
        upload_to="blog/photo",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE
    )
    views_count = models.IntegerField(default=0, verbose_name="просмотры")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]

    def __str__(self):
        return self.title
