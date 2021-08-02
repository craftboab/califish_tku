from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    objects = None
    name = models.CharField('category', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def post_count(self):
    #     n = Post.objects.filter(category = self).count()
    #     return n

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField('name', max_length=50)
    url = models.CharField('url', max_length=200,  null=True, blank=True)
    email = models.EmailField('email', unique=True)
    address = models.CharField('address', max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('name', max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, blank=False)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
