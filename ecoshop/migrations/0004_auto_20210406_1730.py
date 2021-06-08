# Generated by Django 3.1.5 on 2021-04-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0003_auto_20210323_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='Слаг каталога'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='Слаг товара'),
        ),
    ]