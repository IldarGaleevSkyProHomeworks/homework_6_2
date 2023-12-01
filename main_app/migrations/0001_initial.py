# Generated by Django 4.2.7 on 2023-12-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="имя отделения"),
                ),
                ("phones", models.CharField(max_length=255, verbose_name="телефоны")),
                ("address", models.CharField(max_length=255, verbose_name="адрес")),
                (
                    "order",
                    models.IntegerField(default=0, verbose_name="порядок отображения"),
                ),
            ],
            options={
                "verbose_name": "контакт",
                "verbose_name_plural": "контакты",
                "ordering": ("order",),
            },
        ),
    ]