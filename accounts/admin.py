from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import UsersContactPreferences, UsersAdresses



class EmailFilter(SimpleListFilter):
    title = 'Фильтр почты'
    parameter_name = 'user__email'

    def lookups(self, request, model_admin):
        return(
            ('has_email', 'Есть почта'),
            ('no_email', 'Нет почты')
        )

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'has_email':
            return queryset.exclude(user__email = '')
        elif self.value().lower() == 'no_email':
            return queryset.filter(user__email = '')


@admin.register(UsersContactPreferences)
class UsersContactPreferencesAdmin(admin.ModelAdmin):
    fields = ('user', 'phone', 'phone_send', 'whatsapp', 'email_send','instagram', 'instagramm_send')
    # list_filter = (EmailFilter,)
    list_display = list_display_links = ['id', 'user']
    # readonly_fields = ['created', 'get_user_email',]

    def get_user_email(self, user):
        return user.user.email
    
    get_user_email.short_description = "Почта"


@admin.register(UsersAdresses)
class UsersAdressesAdmin(admin.ModelAdmin):
    fields = ('user', 'adress', 'city', 'default_adress',)
    list_display = list_display_links =['id', 'get_user_id', 'user', 'default_adress']
    
    def get_user_id(self, user):
        return user.user.id
    get_user_id.short_description = "ID пользователя"
