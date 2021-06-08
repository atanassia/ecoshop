from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Goods, Category


admin.site.site_header = "Экомагазин"
TEXT_SEC1 = ''' Поля "Имя товара", "Каталог" и "Администратор" обязательны к заполнению. 
                Поле "Слаг" заполняется автоматически, не рекомендуется его изменять.'''
TEXT_SEC4 = 'Поля "Код товара", "Изображение товара" обязательны к заполнению.'

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    fieldsets=(
        ('Секция 1', {
            'fields': (
                'goods_name',
                'category_name',
                'author',
                'status',
                'goods_slug',
                'tags'
            ),
            'description': '%s' % TEXT_SEC1,     
        }),

        ('Секция 2', {
            'fields': ('exposed', 'updated', 'created','likes','total_likes'),
        }),

        ('Секция 3', {
            'fields': ('goods_info', 'manufacturer', 'product_care',),
        }),


        ('Секция 4', {
            'fields' : ('product_code', 'price', 'goods_image','get_image'),
            'description': '%s' % TEXT_SEC4,
        }),
    )
    list_display = ('id', 'goods_name', 'exposed', 'category_name', 'status', 'less_goods_info')
    list_display_links = ('id', 'goods_name',)
    list_filter = ('status','category_name', 'created', 'exposed', 'author')
    search_fields = ('goods_name', 'goods_info')
    raw_id_fields = ('author',)
    prepopulated_fields = {'goods_slug': ('goods_name',)}
    date_hierarchy = 'exposed'
    ordering = ('status', 'exposed')
    readonly_fields = ['get_image', 'created','updated', 'total_likes']

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.goods_image.url} style = " width:500px; height:500px;">')
    get_image.short_description = "Изображение"

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.short_description = 'Количество людей, у кого товар в "Избранное"'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('category_name', 'category_info', 'category_slug', 'category_image', 'get_image')
    readonly_fields = ['get_image']
    list_display = ('category_name', 'category_info')
    search_fields = ('category_name',)
    prepopulated_fields = {'category_slug': ('category_name',)}
    
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.category_image.url} style = " width:500px; height:500px;">')
    
    get_image.short_description = "Изображение"