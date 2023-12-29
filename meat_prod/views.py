from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Promo


def get_home(request):
    title = 'Гланая страница'
    promos = Promo.objects.all()
    return render (request, 'base.html', {'title': title, 'promos': promos})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'category.html',{'categories': categories})


def product_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'category': category, 'products': products })


def products(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products.html', {'product': product})


