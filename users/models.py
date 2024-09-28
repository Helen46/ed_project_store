from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Ведите ваш email"
    )

    phon = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите ваш номер телефона"
    )
    country = models.CharField(
        max_length=150,
        verbose_name="Страна",
        **NULLABLE,
        help_text="Введите название вашей сраны"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        **NULLABLE,
        help_text="Загрузите фото"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Metta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
