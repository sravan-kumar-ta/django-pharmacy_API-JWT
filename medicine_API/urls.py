from django.urls import path
from .views import MedicineList

urlpatterns = [
    path('', MedicineList.as_view())
]
