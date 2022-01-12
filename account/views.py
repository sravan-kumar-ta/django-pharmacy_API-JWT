from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .models import CustomUser
from .CustomBackend import EmailBackend


# Create your views here.
@login_required
def add_admin(request):
    if request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('s_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                               first_name=first_name, user_type=2)
        admin.save()
        return redirect('manage-admin')

    else:
        return render(request, 'admin/admin.html')


@login_required
def manage_admin(request):
    admins = CustomUser.objects.all().filter(user_type=2).order_by("-id")
    return render(request, 'admin/manage_admin.html', {'admins': admins})


@login_required
def update_admin(request, admin_id):
    if request.method == 'POST':
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('s_name')
        username = request.POST.get('username')
        email = request.POST.get('email')

        admin = get_object_or_404(CustomUser, id=admin_id)
        admin.first_name = first_name
        admin.last_name = last_name
        admin.username = username
        admin.email = email
        admin.save()
        return redirect('manage-admin')
    else:
        admin = get_object_or_404(CustomUser, id=admin_id)
        return render(request, 'admin/admin.html', {'admin': admin})


@login_required
def delete_admin(request, admin_id):
    admin = get_object_or_404(CustomUser, id=admin_id)
    admin.delete()
    return redirect('manage-admin')


def register(request):
    if request.method != 'POST':
        return render(request, 'auth/register.html')
    else:
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = CustomUser.objects.create_user(username=username, password=password, email=email, last_name=last_name,
                                               first_name=first_name, user_type=2)
        admin.save()
        return redirect('login')


def do_login(request):
    if request.method != 'POST':
        return render(request, 'auth/login.html')
    else:
        try:
            user = EmailBackend.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid Login... Try again..!")
                return redirect('login')
        except:
            messages.error(request, "Invalid Login... Try again..!")
            return redirect('login')


def do_logout(request):
    logout(request)
    return redirect('login')
