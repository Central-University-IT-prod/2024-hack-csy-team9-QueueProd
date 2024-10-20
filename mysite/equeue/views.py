import datetime
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.shortcuts import render
from .models import Geek

# Create your views here.
def geek_list(request):
    geeks = Geek.objects.filter(create_date__lte=timezone.now()).filter(status=2).order_by('create_date')
    players = Geek.objects.filter(create_date__lte=timezone.now()).filter(status=1).order_by('create_date')
    return render(request, 'equeue/geek_list.html', {'geeks': geeks,'players': players,'now':datetime.datetime.now})