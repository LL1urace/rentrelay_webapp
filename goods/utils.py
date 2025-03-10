from re import search
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery, SearchHeadline

from goods.models import Products
from rentitems.models import RentItems


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    # Запрос для поиска
    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    ) 

    # Запрос для маркировки названия
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow";>',
            stop_sel='</span>',
        )
    ) 
    
    # Запрос для маркировки описания
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow";>',
            stop_sel='</span>',
        )
    )

    return result

    # Старый вариант поиска
    # keywords = [word for word in query.split() if len(word) > 2]
    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(name__icontains=token)
    #     q_objects |= Q(description__icontains=token)

    # return Products.objects.filter(q_objects)


def ri_search(query):
    if query.isdigit() and len(query) <= 5:
        return RentItems.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    # Запрос для поиска
    result = (
        RentItems.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    ) 

    # Запрос для маркировки названия
    result = result.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow";>',
            stop_sel='</span>',
        )
    ) 
    
    # Запрос для маркировки описания
    result = result.annotate(
        bodyline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow";>',
            stop_sel='</span>',
        )
    )

    return result