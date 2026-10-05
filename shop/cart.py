CART_SESSION_ID = 'cart'

def to_int(value):
    text = str(value).replace(',', '').replace('،', '').replace(' ', '')
    if not text:
        return 0
    return int(text)

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = {}
            self.session[CART_SESSION_ID] = cart
        self.cart = cart

    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1):
        pid = str(product_id)
        quantity = max(1, int(quantity))
        current = int(self.cart.get(pid, {}).get('quantity', 0))
        self.cart[pid] = {'quantity': current + quantity}
        self.save()

    def edit(self, product_id, quantity):
        pid = str(product_id)
        if pid not in self.cart:
            return
        quantity = int(quantity)
        if quantity < 1:
            self.delete(product_id)
            return
        self.cart[pid]['quantity'] = quantity
        self.save()

    def delete(self, product_id):
        pid = str(product_id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()

    def clear(self):
        self.cart = {}
        self.save()

    def items(self):
        from .models import Product
        ids = [int(pid) for pid in self.cart.keys()]
        products = {p.id: p for p in Product.objects.filter(id__in=ids)}
        result = []
        for pid, data in self.cart.items():
            product = products.get(int(pid))
            if not product:
                continue
            unit = to_int(product.price)
            qty = to_int(data.get('quantity', 1))  
            result.append({
                'product': product,
                'quantity': qty,
                'unit_price': unit,
                'line_total': unit * qty,
            })
        return result

    def total_price(self):
        return sum(i['line_total'] for i in self.items())

    def total_items(self):
        return sum(i['quantity'] for i in self.cart.values())
