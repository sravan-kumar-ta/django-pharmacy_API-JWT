from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser


# Create your views here.
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


def manage_admin(request):
    admins = CustomUser.objects.all().filter(user_type=2).order_by("-id")
    return render(request, 'admin/manage_admin.html', {'admins': admins})


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


def delete_admin(request, admin_id):
    admin = get_object_or_404(CustomUser, id=admin_id)
    admin.delete()
    return redirect('manage-admin')


def register(request):
    pass


def login(request):
    pass
