from django.shortcuts import render, redirect
from .models import ShopAdmin, CustomUser


# Create your views here.
def home(request):
    if request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('s_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                               first_name=first_name, user_type=1)
        admin.save()
        return redirect('/')

    else:
        return render(request, 'admin/admin.html')
