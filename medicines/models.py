from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name="Category Title")
    slug = models.SlugField(max_length=60, verbose_name="Category Slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Medicine(models.Model):
    title = models.CharField(max_length=100, verbose_name="Medicine Title")
    slug = models.SlugField(max_length=100, verbose_name="Medicine Slug")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='medicines', verbose_name="Medicine Image", blank=True)
    manufactured_by = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(verbose_name="Is Active?")
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
