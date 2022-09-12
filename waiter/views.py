from msilib import add_stream
from django.shortcuts import render
from cashier import models


def waiter(request):
    product = models.Product.objects.all()
    context = { 'product': product}

    return render(request, 'waiter.html', context)