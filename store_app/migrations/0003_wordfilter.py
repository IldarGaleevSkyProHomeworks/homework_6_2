# Generated by Django 4.2.7 on 2023-12-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store_app", "0002_alter_product_preview_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="WordFilter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="название")),
                (
                    "regular_expression",
                    models.CharField(
                        max_length=255, verbose_name="регулярное выражение"
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="комментарий",
                    ),
                ),
                (
                    "is_enable",
                    models.BooleanField(default=True, verbose_name="активно"),
                ),
            ],
            options={
                "verbose_name": "фильтр слов",
                "verbose_name_plural": "фильтры слов",
            },
        ),
    ]