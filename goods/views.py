from django.shortcuts import render

from goods.models import Products



# Create your views here.
def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)  # Убедитесь, что путь корректен

def product(request):
    return render(request, 'goods/product.html')