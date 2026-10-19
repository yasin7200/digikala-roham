from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Product, Category, Monitor, PC

shop_models = {'monitor': Monitor, 'pc': PC}

def pro_view(request, model):
    ct = ContentType.objects.get(app_label='shop', model=model)
    # OR
    # ct = ContentType.objects.get_for_model(shop_models.get(model))
    #------------------------------------------------------------------
    # filterd_products = ct.get_all_objects_for_this_type(brand='brand')
    #OR
    all_pro = ct.model_class().objects.all()
    #OR
    # all_pro = ct.model_class()._default_manager.all()

    return render(request, 'products.html', {
        'all_pro': all_pro
    })


def product_detail(request, model, slug):
    ct = ContentType.objects.get(app_label='shop', model=model)
    product = ct.get_object_for_this_type(slug=slug)
    return render(request, 'detail.html', {'product': product})

def add_to_cart(request):
    pass