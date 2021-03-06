from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
import os
import json
import random
from mainapp.models import Product
from mainapp.models import ProductCategory
from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    main = True
    title = 'Historical games'
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    links_menu = ProductCategory.objects.all()

    services = [
        {
            'name': 'Repreh Qui In Ea Voluptate',
            'link': '/services/1',
            'description': 'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.',
        },
        {
            'name': 'Voluptatibus Maiores Alias',
            'link': '/services/2',
            'description': 'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.',
        },
        {
            'name': 'Aut Perferendis Doloribus',
            'link': '/services/3',
            'description': 'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.',
        },
        {
            'name': 'Dut Aut Reiciendis Maiores',
            'link': '/services/4',
            'description': 'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.',
        },
        {
            'name': 'Maiores Alias Consequatur',
            'link': '/services/5',
            'description': 'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.',
        },
        {
            'name': 'Doloribus Volupta Maiores',
            'link': '/services/6',
            'description': 'Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.',
        },

    ]
    with open(os.path.join(settings.BASE_DIR, 'contacts.json')) as contacts_json_file:
        contacts = json.load(contacts_json_file)

    content = {
        'main': main,
        'title': title,
        'hot_product': hot_product,
        'same_products': same_products,
        'links_menu': links_menu,
        'services': services,
        'contacts': contacts,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    main = False
    title = 'Catalog Historical games'
    with open(os.path.join(settings.BASE_DIR, 'contacts.json')) as contacts_json_file:
        contacts = json.load(contacts_json_file)
    content = {
        'main': main,
        'title': title,
        'contacts': contacts,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/catalog.html', content)


def category_products(request, pk=None):
    main = False
    title = 'Product Historical games'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            category = {'name': 'all'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

    content = {
        'main': main,
        'title': title,
        'links_menu': links_menu,
        'category': category,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/products_list.html', content)


def product(request, pk=None):
    main = False
    title = 'Product Historical games'
    product = get_object_or_404(Product, pk=pk)

    content = {
        'main': main,
        'title': title,
        'product': product,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/product.html', content)


def contacts(request):
    main = False
    title = 'Contacts Historical games'
    with open(os.path.join(settings.BASE_DIR, 'contacts.json')) as contacts_json_file:
        contacts = json.load(contacts_json_file)

    content = {
        'main': main,
        'title': title,
        'contacts': contacts,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contacts.html', content)


def not_found(request, exception):
    main = False
    title = '404'
    products = Product.objects.all()[:4]
    content = {
        'main': main,
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/custom404.html', content)
