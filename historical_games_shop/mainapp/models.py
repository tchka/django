from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя')
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    short_description = models.CharField(max_length=128, blank=True, verbose_name='Краткое описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name
