from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Product, Category


def pro_view(request, model=None):
    if model:
        Model = ContentType.objects.get(app_label='shop', model=model.lower()).model_class()
        qs = Model.objects.select_related('category').all()
    else:
        qs = Product.objects.select_related('category').all()

    cat = request.GET.get('category')
    if cat:
        qs = qs.filter(category_id=cat)

    brand = request.GET.get('brand')
    if brand:
        qs = qs.filter(brand=brand)

    q = request.GET.get('q')
    if q:
        qs = qs.filter(title__icontains=q)

    if request.GET.get('in_stock'):
        qs = qs.filter(counts__gt=0)

    return render(request, 'products.html', {
        'all_pro': qs,
        'categories': Category.objects.all(),
        'brands': Product.objects.values_list('brand', flat=True).distinct(),
    })


def product_detail(request, slug):
    product = get_object_or_404(Product.objects.select_related('category'), slug=slug)
    return render(request, 'detail.html', {'product': product})

def add_to_cart(request):
    pass