# Generated by Django 3.2.20 on 2023-08-11 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_friendly_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]