from django.shortcuts import render

def main(request):
    main = True
    title = 'Historical games'
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
    content = {
        'main': main,
        'title': title,
        'services': services,
    }
    return render(request, 'mainapp/index.html', content)

def catalog(request):
    main = False
    title = 'Catalog Historical games'
    content = {
        'main': main,
        'title': title,
    }
    return render(request, 'mainapp/catalog.html', content)

def product(request):
    main = False
    title = 'Product Historical games'
    content = {
        'main': main,
        'title': title,
    }
    return render(request, 'mainapp/product.html', content)

def contacts(request):
    main = False
    title = 'Contacts Historical games'
    content = {
        'main': main,
        'title': title,
    }
    return render(request, 'mainapp/contacts.html', content)
