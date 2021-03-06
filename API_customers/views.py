from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from medicine_API.models import Order


# Create your views here.
# @login_required
def customer_home(request):
    orders = Order.objects.all()
    return render(request, 'customer/customer.html', {'medicines': orders})
