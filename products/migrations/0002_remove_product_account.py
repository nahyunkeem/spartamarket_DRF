# Generated by Django 4.2 on 2024-09-09 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="account",
        ),
    ]
