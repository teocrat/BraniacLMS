# Generated by Django 4.2.2 on 2023-07-26 11:32

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. ASCII letters and digits only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.ASCIIUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
