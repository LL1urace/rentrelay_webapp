from django.urls import path
from rentitems import views



app_name = 'rentitems'

urlpatterns = [
    path('add_item/', views.add_item, name='add_item'),
    path('add_category/', views.add_category, name='add_category'),
    path('users-rentitems/', views.users_rentitems, name='user_rentitems'),
]