from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название",
        help_text="Введите название"
    )
    content = models.TextField(
        verbose_name="Текст статьи",
        help_text="Введите текст"
    )

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]

    def __str__(self):
        return self.title
