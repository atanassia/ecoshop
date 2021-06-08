from django.contrib.sitemaps import Sitemap
from .models import Goods

class GoodsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Goods.published.all()
    def lastmod(self, obj):
        return obj.updated