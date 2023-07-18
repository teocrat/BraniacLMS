# Generated by Django 4.2.2 on 2023-07-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                (
                    "preamble",
                    models.CharField(max_length=1000, verbose_name="Вступление"),
                ),
                ("body", models.TextField(verbose_name="Содержимое")),
                (
                    "body_as_markdown",
                    models.BooleanField(default=False, verbose_name="Способ разметки"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                ("deleted", models.BooleanField(default=False, verbose_name="Удален")),
            ],
            options={
                "verbose_name": "новость",
                "verbose_name_plural": "новости",
                "ordering": ("-created_at",),
            },
        ),
    ]
