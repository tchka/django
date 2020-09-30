import json
import os

from django.conf import settings
from django.core.management import BaseCommand
from authapp.models import ShopUser
from mainapp.models import Product
from mainapp.models import Contact


FILE_PATH = os.path.join(settings.BASE_DIR, 'mainapp/json')
def load_from_json(file_name):
    with open(os.path.join(FILE_PATH, file_name + '.json')) as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = load_from_json('products')
        contacts = load_from_json('contacts')

        Product.objects.all().delete()
        for item in products:
            Product.objects.create(**item)

        Contact.objects.all().delete()
        Contact.objects.create(**contacts)

        ShopUser.objects.create_superuser(username='django', password='geekbrains', email='', age=30)


