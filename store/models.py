import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("view_category", kwargs={"product_slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    article = models.CharField(max_length=11, verbose_name='Артикул')
    name = models.CharField(max_length=200, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    is_published = models.BooleanField(default=True, verbose_name='В продаже')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    category = TreeForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse("view_product", kwargs={"product_slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    class MPTTMeta:
        order_insertion_by = ['name']

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)
