from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главноая страница приложения - HOME',
        'list': ['first', 'second'],
        'dict': {'fisrt': 1},
        'is_auth': False
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')