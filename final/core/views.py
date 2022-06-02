from django.contrib.auth import authenticate, login as sign_in, logout as sign_out
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from . import models
from rest_framework import viewsets
from .serializers import UserSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')

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
            return render(request, template_name='login.html', context=ctx)
    else:
        return render(request, template_name='login.html', context=ctx)

def logout(request):
    sign_out(request)
    path = request.GET.get('path', None)
    if path is None:
        path = '/'

    return redirect(to=reverse('index'))

def dashboard(request):
    if request.user.is_authenticated:
        devices = models.Device.objects.filter(client=request.user.id)
        users = models.User.objects.select_related('rate').get(id=request.user.id)
        ctx = {
            'devices': devices,
            'user': users.name,
            'rate': users.rate,
        }
        return render(request, template_name='dashboard.html', context=ctx)
    else:
        return redirect(to=reverse('index'))

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all().order_by('name')
    serializer_class = UserSerializer
