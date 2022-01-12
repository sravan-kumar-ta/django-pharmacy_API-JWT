from django.urls import path
from . import views

urlpatterns = [
    path('add_admin/', views.add_admin, name='add-admin'),
    path('manage_admin/', views.manage_admin, name='manage-admin'),
    path('update_admin/<int:admin_id>', views.update_admin, name='update-admin'),
    path('delete_admin/<int:admin_id>', views.delete_admin, name='delete-admin'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]