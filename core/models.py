from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=50, default="Refurbished")
    image_url = models.URLField(max_length=500, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class ServiceRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests', null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    machine_model = models.CharField(max_length=150)
    issue_description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.machine_model}"