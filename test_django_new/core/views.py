from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
#    val = request.GET.get('a', None)
#    val_aa = request.POST.get('a', None)
#    print(val_aa)
    books = models.Book.objects.all()
    ctx = {
        'page_title': 'Test title',
        'aaa': ['bbb','vvvv'],
        'param': True,
        'books': books,
    }
    return render(request, 'index.html', context=ctx)

def gettest(request, param):
    print(param)
    return HttpResponse('Bbbbbb')