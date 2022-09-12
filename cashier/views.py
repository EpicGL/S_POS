from django.shortcuts import render, redirect
from cashier.decorators import allowed_user
from django.contrib.auth.decorators import login_required
from .models import *
from .form import *

@login_required(login_url='login')
@allowed_user(allowed_roles=['cashier'])
def management(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request,'management.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['cashier'])
def inventory(request):
    return render(request,'inventory.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['cashier'])
def sales(request):
    return render(request,'sales.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['cashier'])
def add(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form,}
    return render(request, 'product.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['cashier'])
def edit(request, pk):
    item = Product.objects.get(id=pk)
    form = ProductForm(instance=item)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form, 'item':item}
    print('Unsuccessful :(')
    return render(request, 'product.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['cashier'])
def deleteitem(request, pk):
    item = Product.objects.get(id=pk)
    item.delete()
    return redirect('home')


