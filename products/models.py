from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.Charfield(max_length=254)
    friendly_name = models.Charfield(max_length=254, null=true, blank=True)

    def _str_(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.Charfield(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=true, blank=True)
    image = models.ImageField(null=True, blank=True)

    def _str_(self):
        return self.name