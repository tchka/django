from django.shortcuts import render

def main(request):
    content = {
        'main': True,
    }
    return render(request, 'mainapp/index.html', content)

def catalog(request):
    content = {
        'main': False,
    }
    return render(request, 'mainapp/catalog.html', content)

def product(request):
    content = {
        'main': False,
    }
    return render(request, 'mainapp/product.html', content)

def contacts(request):
    content = {
        'main': False,
    }
    return render(request, 'mainapp/contacts.html', content)
