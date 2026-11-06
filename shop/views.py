from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.contenttypes.models import ContentType
from .models import Product, Category
from django.core.exceptions import ObjectDoesNotExist
from .cart import Cart


def pro_view(request):
    model = request.GET.get('model')
    category_id = request.GET.get('category')

    if model:
        try:
            ct = ContentType.objects.get(app_label='shop', model=model)
            all_pro = ct.model_class().objects.all()
        except ContentType.DoesNotExist:
            all_pro = Product.objects.none()
    else:
        all_pro = Product.objects.all().prefetch_related('images')

    if category_id:
        all_pro = all_pro.filter(category_id=category_id)

    return render(
        request,
        'products.html',
        {
            'all_pro': all_pro,
            'categories': Category.objects.all(),
        },
    )


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {
        'items': cart.items(),
        'total_price': cart.total_price(),
        'total_items': cart.total_items(),
    })


@require_POST
def cart_add(request, product_id):
    quantity = request.POST.get('quantity', 1)
    Cart(request).add(product_id, quantity)
    return redirect('cart')


@require_POST
def cart_update(request, item_id):
    quantity = request.POST.get('quantity', 1)
    Cart(request).edit(item_id, quantity)
    return redirect('cart')


@require_POST
def cart_remove(request, item_id):
    Cart(request).delete(item_id)
    return redirect('cart')


def get_real_product(product):


    for relation in product._meta.related_objects:


        if not (
            relation.one_to_one
            and relation.auto_created
            and getattr(relation.field.remote_field, "parent_link", False)
        ):
            continue

        try:
            child = getattr(product, relation.get_accessor_name())
        except ObjectDoesNotExist:
            continue

        return get_real_product(child)

    return product


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)


    real_product = get_real_product(product)

    specifications = []

    for field in real_product._meta.concrete_fields:


        if field.model == Product:
            continue


        if field.primary_key or getattr(
            field.remote_field, "parent_link", False
        ):
            continue

        value = getattr(real_product, field.name)


        if field.choices:
            value = getattr(
                real_product,
                f"get_{field.name}_display"
            )()


        elif field.get_internal_type() == "BooleanField":
            value = "بله" if value else "خیر"


        if value is None or value == "":
            continue

        specifications.append({
            "label": field.verbose_name,
            "value": value,
        })

    return render(request, "detail.html", {
        "product": product,
        "specifications": specifications,
        "images": product.images.all(),
    })
