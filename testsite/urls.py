from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from ecoshop.sitemaps import GoodsSitemap

sitemaps = {
    'goods': GoodsSitemap,
}


urlpatterns = [
    path('', include('ecoshop.urls', namespace = '')),
    path('', include('accounts.urls', namespace = '')),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'ecoshop.views.page_not_found'