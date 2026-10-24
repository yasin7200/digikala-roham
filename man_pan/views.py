from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from account.models import User
from shop.models import Product, Category


def is_manager(user):
    """Only staff/superusers and manager group members can access the panel."""
    if not user.is_authenticated:
        return False
    if user.is_staff or user.is_superuser:
        return True
    return user.groups.filter(name='manager').exists()


@user_passes_test(is_manager, login_url='login')
def manage_view(request):
    # ---------- User statistics ----------
    total_users = User.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    staff_users = User.objects.filter(is_staff=True).count()
    customer_users = User.objects.filter(
        groups__name='customer'
    ).distinct().count()

    # Recently joined users (latest 5)
    recent_users = User.objects.order_by('-date_join')[:5]

    # ---------- Product / catalogue statistics ----------
    total_products = Product.objects.count()
    total_categories = Category.objects.count()

    # Stock health
    low_stock_products = Product.objects.filter(
        counts__gte=1, counts__lte=5
    ).order_by('counts')[:5]
    out_of_stock_products = Product.objects.filter(counts=0)[:5]

    # Categories with product counts
    categories_with_counts = Category.objects.all()

    # Top rated products
    top_rated_products = Product.objects.order_by('-rate')[:5]

    context = {
        'total_users': total_users,
        'active_users': active_users,
        'staff_users': staff_users,
        'customer_users': customer_users,
        'recent_users': recent_users,
        'total_products': total_products,
        'total_categories': total_categories,
        'low_stock_products': low_stock_products,
        'out_of_stock_products': out_of_stock_products,
        'categories_with_counts': categories_with_counts,
        'top_rated_products': top_rated_products,
    }

    return render(request, 'man_pan.html', context)
