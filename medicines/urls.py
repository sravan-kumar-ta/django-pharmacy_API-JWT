from django.urls import path, include
from medicines import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/', views.medicine, name='manage-medicine'),
    path('add_medicine/', views.add_medicine, name='add-medicine'),
    path('update_medicine/<int:m_id>/', views.update_medicine, name='update-medicine'),
    path('delete_medicine/<int:m_id>/', views.delete_medicine, name='delete-medicine'),
    path('admins/', include('account.urls')),
    path('customers/', include('API_customers.urls'))
]
