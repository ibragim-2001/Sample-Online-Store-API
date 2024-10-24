from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category', verbose_name='Категория')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления товара')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['create_at', ]


    def __str__(self):
        return self.title
