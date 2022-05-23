from django.contrib.auth import authenticate, login as sign_in, logout as sign_out
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from . import models

# Create your views here.

def index(request):
#    val = request.GET.get('a', None)
#    val_aa = request.POST.get('a', None)
#    print(val_aa)
    # b_ctx = []
    books = models.Book.objects.all()
    # for b in books:
    #     b_ctx += [{
    #         'name': b.name,
    #         'author': b.author,
    #         'linked_by': models.BookUsers.objects.filter(book=b)
    #     }]
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

def login(request):
    ctx = {}
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        if email and password:
            user = authenticate(request, username=email, password=password)
        else:
            ctx.update({'error':'Форма содержит пустые поля'})
        if user is not None and user.is_active:
            sign_in(request, user)
            return redirect(to=reverse('index'))
        else:
            ctx.update({'error':'Пользователь не активен'})
        pass
    else:
        return render(request, template_name='login.html', context=ctx)

def logout(request):
    sign_out(request)
    path = request.GET.get('path', None)
    if path is None:
        path = '/'

    return redirect(to=reverse('index'))