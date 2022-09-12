from django.shortcuts import render

def kitchen(request):
    context = {}
    return render(request, 'kitchen.html', context)