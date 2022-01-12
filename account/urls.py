from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add_admin/', views.add_admin, name='add-admin'),
    path('manage_admin/', views.manage_admin, name='manage-admin'),
    path('update_admin/<int:admin_id>/', views.update_admin, name='update-admin'),
    path('delete_admin/<int:admin_id>/', views.delete_admin, name='delete-admin'),
    path('login/', views.do_login, name='login'),
    path('register/', views.register, name='registration'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),
]
