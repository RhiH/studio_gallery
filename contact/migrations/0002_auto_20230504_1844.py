# Generated by Django 3.2.17 on 2023-05-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default='b', max_length=255),
            preserve_default=False,
        ),
    ]
