# Generated by Django 3.2.17 on 2023-06-30 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_auto_20230629_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artists',
            name='category',
        ),
    ]