from django import template
from django.utils.http import urlencode

from goods.models import Categories
from rentitems.models import RentCategories


register = template.Library()



@register.simple_tag()
def tag_categories():
    # Получаем все категории из обеих моделей
    categories = list(Categories.objects.all()) + list(RentCategories.objects.all())
    return categories



@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)