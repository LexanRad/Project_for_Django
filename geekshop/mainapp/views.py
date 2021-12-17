from django.shortcuts import render

from mainapp.models import Product


def products(request):
    title = 'каталог'
    links_menu = [
        {'href': 'products/', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    products_1 = Product.objects.all()[:3]

    context = {
        'title': title,
        'links_menu': links_menu,
        'products_1': products_1
    }
    return render(request, 'mainapp/products.html', context=context)
# Create your views here.
