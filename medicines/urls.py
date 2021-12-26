from django.urls import path
from account import admin_views
from medicines import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/', views.medicine, name='manage-medicine'),
    path('add_medicine/', views.add_medicine, name='add-medicine'),
    path('update_medicine/<int:m_id>/', views.update_medicine, name='update-medicine'),
    path('delete_medicine/<int:m_id>/', views.delete_medicine, name='delete-medicine'),

    # ####___admin urls___#### #
    path('add_admin/', admin_views.add_admin, name='add-admin'),
    path('manage_admin/', admin_views.manage_admin, name='manage-admin'),
    path('update_admin/<int:admin_id>', admin_views.update_admin, name='update-admin'),
    path('delete_admin/<int:admin_id>', admin_views.delete_admin, name='delete-admin')
]
