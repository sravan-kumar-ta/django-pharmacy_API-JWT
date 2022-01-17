from django.urls import path
from .views import MedicineList, OrderView, OrderedList

urlpatterns = [
    path('', MedicineList.as_view()),
    path('buy/', OrderView.as_view()),
    path('orders/', OrderedList.as_view())
]
