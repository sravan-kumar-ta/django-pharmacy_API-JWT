from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name="Category Title")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Medicine(models.Model):
    title = models.CharField(max_length=100, verbose_name="Medicine Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='medicines', verbose_name="Medicine Image", blank=True)
    manufactured_by = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(verbose_name="Is Active?", default=True)
    stock = models.IntegerField(default=10)

    def __str__(self):
        return self.title
