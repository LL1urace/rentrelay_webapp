from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Магазин мебели HOME',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том почему такой классный сайт для аренды вещей.'
    }
    return render(request, 'main/about.html', context)