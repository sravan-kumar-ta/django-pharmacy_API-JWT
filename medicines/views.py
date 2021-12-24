from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from .models import Medicine, Category


# Create your views here.
def home(request):
    return render(request, 'home.html')


def medicine(request):
    medicines = Medicine.objects.all().order_by('-id')
    return render(request, 'manage_medicine.html', {'medicines': medicines})


def add_medicine(request):
    if request.method == 'POST':
        name = request.POST.get('m_name')
        category_id = request.POST.get('category')
        image = request.FILES['medicine_image']
        manufacture = request.POST.get('manufacture')
        price = request.POST.get('price')
        is_active = request.POST.get('active')

        slug = slugify(name)
        category = get_object_or_404(Category, id=category_id)
        if is_active == 'on':
            is_active = 'True'
        else:
            is_active = 'False'
        medicine = Medicine(title=name, slug=slug, category=category, image=image, manufactured_by=manufacture, price=price, is_active=is_active)
        medicine.save()
        # return HttpResponseRedirect('/')
        return render(request, 'add_medicine.html')
    else:
        categ = Category.objects.all()
        return render(request, 'add_medicine.html', {'categories': categ})


def update_medicine(request, m_id):
    if request.method != 'POST':
        item = get_object_or_404(Medicine, id=m_id)
        category = Category.objects.all()
        return render(request, 'add_medicine.html', {'medicine': item, 'categories': category})
    else:
        item = get_object_or_404(Medicine, id=m_id)
        name = request.POST.get('m_name')
        category_id = request.POST.get('category')
        # image = request.FILES['medicine_image']
        manufacture = request.POST.get('manufacture')
        price = request.POST.get('price')
        is_active = request.POST.get('active')

        slug = slugify(name)
        category = get_object_or_404(Category, id=category_id)
        if is_active == 'on':
            is_active = 'True'
        else:
            is_active = 'False'

        item.title = name
        item.slug = slug
        item.category = category
        item.manufactured_by = manufacture
        item.price = price
        item.is_active = is_active
        item.save()

        return redirect('manage-medicine')
