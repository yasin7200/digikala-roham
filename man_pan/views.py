from django.shortcuts import render
from account.models import User

def manage_view(request):
    context = {
        'user.count': User.objects.all().count(),
        'active_customer': User.objects.filter(groups__name='customer')
    }

    return render(request, 'man_pan.html', context)
