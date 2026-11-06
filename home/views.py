from shop.models import Product, Category
from django.shortcuts import render


def home_view(request):
    latest_products = Product.objects.order_by('-id')[:8]
    categories = Category.objects.all()
    brands = (
        Product.objects.exclude(brand__isnull=True)
        .exclude(brand__exact='')
        .order_by('brand')
        .values_list('brand', flat=True)
        .distinct()
    )

    return render(request, 'home.html', {
        'latest_products': latest_products,
        'categories': categories,
        'brands': brands,
    })
