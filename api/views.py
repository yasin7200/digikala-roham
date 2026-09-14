from django.shortcuts import render

def list_person_view(request):
    return render(request, 'lp.html')
