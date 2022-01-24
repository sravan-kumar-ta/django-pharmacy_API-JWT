from django.contrib import admin
from .models import Category, Medicine


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class MedicineAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'price']
    list_editable = ['is_active', 'price']
    list_filter = ('category', 'is_active')
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)
admin.site.register(Medicine, MedicineAdmin)
