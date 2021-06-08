from django.urls import path
from . import views

from accounts.views import login_view, logout_view, register_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ecoshop'

urlpatterns = [
    path('', views.test, name ='test'),
    path('search/', views.search, name='search'),
    path('search/<slug:tag_slug>/', views.search, name='search'),
    path('catalogs/', views.catalogs_list, name = 'catalogs_list'),
    path('catalogs/<slug:category>/', views.goods_list, name = 'goods_list'),
    path('catalogs/<slug:category_slug>/<slug:goods_slug>/', views.goods_detail, name = 'goods_detail'),
    path('like/', views.like_goods, name = 'like_goods'),
    path('error404/', views.page_not_found),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)