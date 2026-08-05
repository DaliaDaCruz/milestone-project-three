from django.db import models
from django.contrib.auth.models import User


class Machine(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    specs = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='machines/', blank=True, null=True)

    def get_image_url(self):
        """Returns media URL if file exists, else falls back to static path."""
        try:
            if self.image and self.image.name:
                return self.image.url
        except Exception:
            pass
        return f"/static/core/machines/{self.slug}.png"

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.name} - {self.service}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    badge = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_number = models.CharField(
        max_length=32, unique=True, editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order_number} by {self.full_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items'
    )
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return (
            f"{self.quantity} x {self.machine.name} "
            f"(Order #{self.order.order_number})"
        )
    