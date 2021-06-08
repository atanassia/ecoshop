from django.shortcuts import render, get_object_or_404, redirect
from random import randint
from django.db.models import Q

from django.http import HttpResponse
from .models import Goods, Category
from taggit.models import Tag

from business_services import ecoshop_services


def test(request):
    return render(request, 'ecoshop/test.html')


def index(request):       
    return render(request, 'layout/base.html')


def catalogs_list(request):
    catalogs = Category.objects.all()
    context = {'catalogs':catalogs}
    return render(request, 'ecoshop/catalog.html', context)

def goods_list(request, category):
    goods = Goods.published.filter(category_name_id = Category.objects.get(category_slug = category).pk)
    category = Category.objects.get(category_slug = category)
    context = {'goods':goods, 'category':category}
    return render(request, 'ecoshop/goods_list.html', context)


def goods_detail(request, category_slug, goods_slug):
    # goods = Goods.published.get(goods_slug = goods_slug)
    goods = get_object_or_404(Goods, goods_slug = goods_slug)
    is_liked = False
    if goods.likes.filter(id = request.user.id).exists():
        is_liked = True
    active = 'active'
    list_goods_category = ecoshop_services.goods_accardion(goods_slug)
    context = {'goods':goods, 'list_goods_category':list_goods_category, 'active':active, 'is_liked':is_liked}
    return render(request, 'ecoshop/goods_page.html', context)


def like_goods(request):
    goods = get_object_or_404(Goods, id = request.POST.get('goods_id'))
    if goods.likes.filter(id = request.user.id).exists():
        goods.likes.remove(request.user)
        is_liked = False
    else:
        goods.likes.add(request.user)
        is_liked = True
    return redirect(goods.get_absolute_url())


def search(request, tag_slug = None):
    smile = ecoshop_services.smile()
    catalogs = goods = None
    if request.method == "POST":
        searched = request.POST['searched']
        catalogs = Category.objects.filter(category_name__icontains=searched)
        goods = Goods.published.filter(Q(goods_name__icontains=searched) | Q(goods_info__icontains = searched))
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        goods = Goods.published.filter(tags__in=[tag])
        catalogs = searched = None
    context = {'catalogs':catalogs, 'goods':goods, 'searched': searched, 'smile':smile, 'tag':tag}          
    return render(request, 'ecoshop/search.html', context)


def page_not_found(request, exception = None):
    return render(request, 'ecoshop/404.html')
