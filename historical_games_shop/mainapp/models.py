from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание категории')
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
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
        return f'{self.name} ({self.category.name})'
        # return f'{self.name}'

class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Gallery')
    is_main = models.BooleanField(default=False);
    image = models.ImageField(upload_to='product_images', blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя')
    address = models.CharField(max_length=128, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=64, blank=True, verbose_name='Телефон')
    fax = models.CharField(max_length=64, blank=True, verbose_name='Факс')
    email = models.CharField(max_length=64, blank=True, verbose_name='E-mail')

    def __str__(self):
        return f'Contacts {self.name}'