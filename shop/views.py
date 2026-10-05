from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Product, Category
from .cart import Cart


def pro_view(request):
    all_pro = Product.objects.select_related('category').all()
    categories = Category.objects.all()
    brands = Product.objects.values_list('brand', flat=True).distinct()
    return render(request, 'products.html', {
        'all_pro': all_pro,
        'categories': categories,
        'brands': brands,
    })


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {
        'items': cart.items(),
        'total_price': cart.total_price(),
        'total_items': cart.total_items(),
    })

def product_detail_view(request, slg):
    product = Product.objects.get(slug=slg)
    return render(request, 'detail.html', {'product':product})

@require_POST
def cart_add(request, product_id):
    Cart(request).add(product_id, request.POST.get('quantity', 1))
    return redirect('cart')


@require_POST
def cart_update(request, item_id):
    Cart(request).edit(item_id, request.POST.get('quantity', 1))
    return redirect('cart')


@require_POST
def cart_remove(request, item_id):
    Cart(request).delete(item_id)
    return redirect('cart')


@require_POST
def cart_clear(request):
    Cart(request).clear()
    return redirect('cart')
