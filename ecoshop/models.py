from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(Q(status='в наличии') | Q(status='под заказ') | Q(status='нет в наличии'))

class Goods(models.Model):
    STATUS_CHOICES = (
        ('ожидается', 'Ожидается'),
        ('в наличии', 'В наличии'),
        ('под заказ', 'Под заказ'),
        ('нет в наличии', 'Нет в наличии'),
    )
    goods_name = models.CharField(max_length = 70, verbose_name='Имя товара')
    goods_info = models.TextField(blank = True, verbose_name='Описание товара') 
    manufacturer = models.TextField(blank = True, verbose_name='Производитель товара') 
    product_care = models.TextField(blank = True, verbose_name='Уход') 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eco_goods', verbose_name = 'Администратор')
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True, verbose_name = 'В избранном')
    goods_image = models.ImageField(upload_to = 'images/goods/%Y/%m', verbose_name = 'Изображение товара')
    product_code = models.CharField(max_length = 15, verbose_name='Код товара')
    price = models.FloatField(null = True, blank = True, verbose_name='Цена')
    exposed = models.DateTimeField(default=timezone.now, verbose_name= 'Выставлен')
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name= 'Обновлен')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ожидается', verbose_name = 'Статус')
    #FIXME:Убрать null = True и убрать "name" в FK !!!!!!
    category_name = models.ForeignKey('Category', null = True, on_delete=models.PROTECT, verbose_name = 'Каталог')
    goods_slug = models.SlugField(max_length=250, unique = True, verbose_name = 'Слаг товара')
    tags = TaggableManager()
    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ('-exposed',)

    def __str__(self):
        return self.goods_name
    
    def get_absolute_url(self):
        return reverse("ecoshop:goods_detail", args=[self.category_name.category_slug, self.goods_slug])

    def info_as_list(self):
        return self.goods_info.split('\n')

    def less_goods_info(self):
        return u"%s..." % (self.goods_info[:150],)


class Category(models.Model):
    category_name = models.CharField(max_length = 70, verbose_name='Каталог')
    category_info = models.TextField(blank = True, verbose_name='Иформация о каталоге') 
    category_image = models.ImageField(upload_to = 'images/categories', verbose_name = 'Изображение категории')
    category_slug = models.SlugField(max_length=250, unique = True, verbose_name = 'Слаг каталога')
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Каталоги"
        verbose_name = "Каталог"
        ordering = ('category_name',)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("ecoshop:goods_list", args=[self.category_name.category_slug])




