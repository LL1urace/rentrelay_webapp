from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RentCategoryForm, RentItemForm
from .models import RentItems, RentCategories
from django.contrib.auth.decorators import login_required

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = RentCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rentitems:user_rentitems')
    else:
        form = RentCategoryForm()
    
    return render(request, 'rentitems/add_category.html', {'form': form})

def add_item(request):
    if request.method == 'POST':
        form = RentItemForm(request.POST, request.FILES)
        if form.is_valid():
            rent_item = form.save(commit=False)
            rent_item.owner = request.user  # Привязываем товар к текущему пользователю
            rent_item.save()
            return redirect('rentitems:user_rentitems')
    else:
        form = RentItemForm()
    
    return render(request, 'rentitems/add_item.html', {'form': form})

def remove_item(request):
    # Получаем id товара из POST-запроса
    rent_item_id = request.POST.get("rent_item_id")
    rent_item = RentItems.objects.get(id=rent_item_id, owner=request.user)
    
    # Удаляем товар
    rent_item.delete()

    # Обновляем список товаров пользователя
    rent_items = RentItems.objects.filter(owner=request.user)
    return render(request, 'rentitems/users-rentitems.html', {'rent_items': rent_items})

@login_required
def users_rentitems(request):
    rent_items = RentItems.objects.filter(owner=request.user)
    return render(request, 'rentitems/users-rentitems.html', {'rent_items': rent_items})