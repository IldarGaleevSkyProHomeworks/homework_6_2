# Generated by Django 4.2.7 on 2023-11-17 04:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=250, verbose_name="наименование")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=1024, null=True, verbose_name="описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=250, verbose_name="наименование")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=1024, null=True, verbose_name="описание"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=12,
                        verbose_name="цена",
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="дата создания"
                    ),
                ),
                (
                    "modify_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="дата изменения"
                    ),
                ),
                (
                    "preview_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="product_preview_images/",
                        verbose_name="изображение",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.category",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "товар",
                "verbose_name_plural": "товары",
                "ordering": ("name", "price", "create_date", "modify_date", "category"),
            },
        ),
    ]