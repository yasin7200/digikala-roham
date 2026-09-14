from django.shortcuts import render
from . models import Product, Category

def pro_view(request):
    all_pro = Product.objects.select_related('category').all()
    categories = Category.objects.all()
    brands = Product.objects.values_list('brand', flat=True).distinct()

    return render(request, 'products.html', {
        'all_pro': all_pro,
        'categories': categories,
        'brands': brands,
    })