from django.urls import path

from API_customers import views

urlpatterns = [
    path('', views.customer_home, name='customer-home'),
]
