from django.shortcuts import render
from shop.models import Product, Category


def home_view(request):
    return render(request, 'home.html', {
        'categories': Category.objects.all(),
        'products': Product.objects.select_related('category').all()[:12],
    })
