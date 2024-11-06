import uuid

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена') 
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category', verbose_name='Категория')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-create_at', ]


    def save(self, *args, **kwargs):
        if not self.slug.endswith('-product'):
            self.slug = slugify(self.title + '-' + str(uuid.uuid4())+ '-' + 'products')
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзины пользователей'

    def __str__(self):
        return str(self.id)
    

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.IntegerField(default=0)