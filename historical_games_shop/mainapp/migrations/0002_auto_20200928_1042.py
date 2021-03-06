# Generated by Django 2.2 on 2020-09-28 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=128, verbose_name='Краткое описание'),
        ),
    ]
