# Generated by Django 3.1.5 on 2021-05-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210513_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscontactpreferences',
            name='instagramm_send',
            field=models.BooleanField(default=False, verbose_name='Связь по инстаграмму'),
        ),
        migrations.AddField(
            model_name='userscontactpreferences',
            name='phone_send',
            field=models.BooleanField(default=False, verbose_name='Связь по номеру телефона'),
        ),
        migrations.AlterField(
            model_name='userscontactpreferences',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Истаграмм'),
        ),
        migrations.AlterField(
            model_name='userscontactpreferences',
            name='whatsapp',
            field=models.BooleanField(default=False, verbose_name='Связь по вотсаппу'),
        ),
    ]
