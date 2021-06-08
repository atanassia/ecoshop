from ecoshop.models import Goods, Category
from random import randint, choice
from django.shortcuts import get_object_or_404


def goods_accardion(goods_slug):
    goods = get_object_or_404(Goods, goods_slug = goods_slug)
    #создаю список с id всех каталогов
    catl1 = [t for t in Category.objects.values_list('id', flat = True)]
    catl = []
    #проверяю, не пустые ли они
    for i in catl1:
        if Goods.published.filter(category_name_id = i):
            catl.append(i)
    list_goods_category = [[0,0,0], [0,0,0], [0,0,0]]
    for item in range(3):
        #выбираю рандомный каталог
        category_choice = choice(catl)
        #удаляю его
        catl.remove(category_choice)
        #создаю список товаров этого каталога
        goodsl = [r for r in Goods.published.filter(category_name_id = category_choice).values_list('id', flat=True)]
        #удаляю тот товар, на странице которого щас нахожусь
        if goods.id in goodsl:
            goodsl.remove(goods.id)
        for i in range(3):
            goods_choice = choice(goodsl)
            goods_acc = Goods.published.get(id = goods_choice)
            list_goods_category[i][item] = goods_acc
            goodsl.remove(goods_choice)
    return list_goods_category


def smile():
    smile_dict = {
        1:"(´• ω •)", 2:"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧", 3:"ʕ ᵔᴥᵔ ʔ", 4:"( ˙꒳​˙ )", 5:"╰(▔∀▔)╯", 6:"(◕‿◕)", 7:"°˖✧◝(⁰▿⁰)◜✧˖°", 
        8:"(ง ื▿ ื)ว", 9:"(づ￣ ³￣)づ", 10:"(^=◕ᴥ◕=^)", 11:"_(:3 」∠)_",
    }
    smile = smile_dict[randint(1, len(smile_dict))]
    return smile