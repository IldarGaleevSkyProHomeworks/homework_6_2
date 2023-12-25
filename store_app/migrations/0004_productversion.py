# Generated by Django 4.2.7 on 2023-12-24 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("store_app", "0003_wordfilter"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductVersion",
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
                    "version_name",
                    models.CharField(max_length=150, verbose_name="название версии"),
                ),
                (
                    "version_number",
                    models.IntegerField(default=0, verbose_name="номер версии"),
                ),
                ("is_latest", models.BooleanField(verbose_name="последняя версия")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="store_app.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия продукта",
                "verbose_name_plural": "версии продукта",
            },
        ),
    ]