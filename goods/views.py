from django.http import Http404
from django.shortcuts import get_object_or_404, render

from goods.models import Products



# Create your views here.
def catalog(request, category_slug):

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        # Код в уроке не работал
        # goods= get_object_or_404(Products.objects.filter(category__slug=category_slug))
        # Фильтруем товары в существующей категории
        goods = Products.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404("No products found in this category.")

    context = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)  # Убедитесь, что путь корректен

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'goods/product.html', context=context)