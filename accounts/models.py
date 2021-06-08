from django.db import models
from django.contrib.auth.models import User


class UsersContactPreferences(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    phone = models.CharField(max_length = 200, blank = True, default='', verbose_name="Номер")
    phone_send = models.BooleanField(default= False, verbose_name="Связь по номеру телефона")
    whatsapp = models.BooleanField(default= False, verbose_name="Связь по вотсаппу")
    email_send = models.BooleanField(default= False, verbose_name="Связь по почте")
    instagram = models.CharField(max_length = 100, default = '', blank = True, verbose_name="Истаграм")
    instagramm_send = models.BooleanField(default= False, verbose_name="Связь по инстаграму")

    class Meta:
        verbose_name_plural = 'Способы связи'
        verbose_name = 'Способ связи'
        ordering = ('user',)

    def __str__(self):
        return self.user.username


class UsersAdresses(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    adress = models.CharField(max_length=255, blank = False, verbose_name='Адрес')
    city = models.CharField(max_length=120, blank = False, verbose_name='Город')
    default_adress = models.BooleanField(default = False, verbose_name = 'Адрес по умлочанию')

    class Meta:
        verbose_name_plural = 'Адреса'
        verbose_name = 'Адрес'
        ordering = ('user', '-default_adress')

    def __str__(self):
        return self.user.username
