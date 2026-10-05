from .cart import Cart


def cart_context(request):
    cart = Cart(request)
    return {
        'cart_total_items': cart.total_items(),
        'cart_total_price': cart.total_price(),
    }
