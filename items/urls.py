from django.urls import path
from items import views



app_name = 'items'

urlpatterns = [
    path('item_add/', views.item_add, name='item_add'),
    path('item_remove/', views.item_remove, name='item_remove'),
]