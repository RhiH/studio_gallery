# Generated by Django 3.2.17 on 2023-05-09 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='biography',
        ),
    ]