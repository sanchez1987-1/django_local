from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    val = request.GET.get('a', None)
    val_aa = request.POST.get('a', None)
    print(val_aa)
    
    return HttpResponse('Aaaaa')

def gettest(request, param):
    print(param)
    return HttpResponse('Bbbbbb')