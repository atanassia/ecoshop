# Generated by Django 3.1.5 on 2021-05-13 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210511_2050'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usersadresses',
            unique_together=set(),
        ),
    ]
