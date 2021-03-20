from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Destination

def index(request):


    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})



