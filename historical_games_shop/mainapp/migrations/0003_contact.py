# Generated by Django 2.2 on 2020-09-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200928_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Имя')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, max_length=64, verbose_name='Телефон')),
                ('fax', models.CharField(blank=True, max_length=64, verbose_name='Факс')),
                ('email', models.CharField(blank=True, max_length=64, verbose_name='E-mail')),
            ],
        ),
    ]