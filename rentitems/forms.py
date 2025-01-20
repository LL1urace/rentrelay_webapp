from django import forms
from .models import RentCategories, RentItems
from goods.models import Categories
from itertools import chain


class RentCategoryForm(forms.ModelForm):
    class Meta:
        model = RentCategories
        fields = ['name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название категории'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите URL для категории'}),
        }


class RentItemForm(forms.ModelForm):
    class Meta:
        model = RentItems
        fields = ['name', 'description', 'price_per_day', 'deposit', 'available', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание товара'}),
            'price_per_day': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена за день аренды'}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Залоговая сумма'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'})
        }
    
    def __init__(self, *args, **kwargs):
        super(RentItemForm, self).__init__(*args, **kwargs)

        # Получаем объекты категорий из обеих моделей
        rent_categories = RentCategories.objects.all()
        product_categories = Categories.objects.all()

        # Создаем кортежи (id, название) для каждой категории из обеих моделей
        rent_category_choices = [(cat.id, cat.name) for cat in rent_categories]
        product_category_choices = [(cat.id, cat.name) for cat in product_categories]

        # Объединяем выборки категорий
        combined_choices = rent_category_choices + product_category_choices

        # Используем объединённый список для поля 'category'
        self.fields['category'].choices = combined_choices