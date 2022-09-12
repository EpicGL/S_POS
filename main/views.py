from django.shortcuts  import redirect

def home(request):
    if request.user.is_authenticated:
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'kitchen':
            return redirect('kitchen/')
        elif group == 'waiter':
            return redirect('waiter/')
        elif group == 'cashier':
            return redirect('management/')
        elif group == 'admin':
            return redirect('management/')
    else:
       return redirect('login/')
