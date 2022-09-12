from urllib import request
from django.shortcuts import render
from django.urls import is_valid_path
from .decorators import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                group = None
                if request.user.groups.exists():
                    group = request.user.groups.all()[0].name
                if group == 'kitchen':
                    return redirect('kitchen/')
                elif group == 'waiter':
                    return redirect('waiter/')
                elif group == 'cashier':
                    return redirect('admin/')
            else:
                messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'login.html', context)


def logOut(request):
    logout(request)
    return redirect ('login')

