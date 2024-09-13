# Generated by Django 5.1.1 on 2024-09-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_is_published_blog_slug_blog_views_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите изображение",
                null=True,
                upload_to="blog/photo",
                verbose_name="Изображение",
            ),
        ),
    ]
