# Generated by Django 4.2 on 2024-04-25 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ('id',), 'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
    ]
