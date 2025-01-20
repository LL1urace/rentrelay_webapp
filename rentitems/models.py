from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()  # Получение пользовательской модели

# Модель категорий для продуктов в аренду
class RentCategories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'rent_category'
        verbose_name = 'Категория для аренды'
        verbose_name_plural = 'Категории для аренды'

    def __str__(self):
        return self.name

# Модель продуктов для аренды
class RentItems(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='rent_items_images', blank=True, null=True, verbose_name='Изображение')
    price_per_day = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена за день аренды')
    deposit = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Залоговая сумма')
    available = models.BooleanField(default=True, verbose_name='Доступен для аренды')
    category = models.ForeignKey(to=RentCategories, on_delete=models.CASCADE, verbose_name='Категория')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Владелец продукта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        db_table = 'rent_item'
        verbose_name = 'Продукт в аренду'
        verbose_name_plural = 'Продукты в аренду'
        ordering = ("-created_at",)

    def __str__(self):
        return f'{self.name} - Владелец: {self.owner.username}'
    
    # def get_absolute_url(self):
    #     return reverse("rentitems:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def rent_price(self, days):
        """Вычисляет стоимость аренды за заданное количество дней."""
        return round(self.price_per_day * days, 2)