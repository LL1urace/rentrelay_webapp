from django.http import JsonResponse
from django.shortcuts import render, redirect
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

@login_required
def users_rentitems(request):
    rent_items = RentItems.objects.filter(owner=request.user)
    return render(request, 'rentitems/users-rentitems.html', {'rent_items': rent_items})