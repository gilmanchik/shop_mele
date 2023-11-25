from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import *


def product_list(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        products = products.filter(category=category)
    context = {'category': category,
               'products': products,
               'categories': categories}
    return render(request, 'shop/product_list.html', context)


def product_detail(request, id, slug):
    products = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_add_form = AddProductForm()
    context = {'products': products, 'cart_add_form': cart_add_form}
    return render(request, 'shop/product_detail.html', context)
