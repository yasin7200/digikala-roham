from django.shortcuts import render

from shop.models import Category, Product


def home_view(request):
    categories = Category.objects.all()
    featured_products = Product.objects.select_related('category').all()[:8]
    latest_products = Product.objects.select_related('category').all().order_by('-id')[:8]
    return render(request, 'home.html', {
        'categories': categories,
        'featured_products': featured_products,
        'latest_products': latest_products,
    })
