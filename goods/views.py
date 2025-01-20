from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render

from goods.models import Products
from rentitems.models import RentItems
from goods.utils import q_search, ri_search



# Create your views here.
def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    

    if category_slug == 'all':
        goods = Products.objects.all()
        rent_items = RentItems.objects.all()
    elif query:
        goods = q_search(query)
        rent_items = ri_search(query)
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        rent_items = RentItems.objects.filter(category__slug=category_slug)

    # Объединяем товары только если обе модели не пусты
    if rent_items.exists() and goods.exists():
        all_goods = list(rent_items) + list(goods)
    elif rent_items.exists():
        all_goods = list(rent_items)
    else:
        all_goods = list(goods)
    
    # Применяем фильтрацию по скидке
    if on_sale:
        all_goods = [item for item in all_goods if item.discount > 0]

    # Применяем сортировку, если указано
    if order_by and order_by != "default":
        all_goods = sorted(all_goods, key=lambda x: getattr(x, order_by))

    # if on_sale:
    #     goods = goods.filter(discount__gt=0)

    # if order_by and order_by != "default":
    #     goods = goods.order_by(order_by)
    
    paginator = Paginator(all_goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'R&R',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)  # Убедитесь, что путь корректен

def product(request, product_slug):
    # Пробуем получить продукт, если не находим, ищем RentItem
    try:
        product = Products.objects.get(slug=product_slug)
        is_product = True  # Устанавливаем флаг, что это продукт
    except Products.DoesNotExist:
        product = get_object_or_404(RentItems, slug=product_slug)  # Если не нашли продукт, ищем RentItem
        is_product = False  # Устанавливаем флаг, что это RentItem

    context = {
        'product': product,
        'is_product': is_product  # Передаем в шаблон, чтобы различать, что это за объект
    }
    return render(request, 'goods/product.html', context)