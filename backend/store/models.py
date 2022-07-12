from django.contrib.auth.models import User

from django.db import models
from django.urls import reverse

# Category model db use as ForeignKey
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    # Instructions for the db model
    class Meta:
        verbose_name_plural = 'categories'

    # Return absolute url
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])
    

    # Return the name of the category
    def __str__(self):
        return self.name     


# We've got the product right?
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_creator")
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Extra instructions
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    #Return the URL
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title