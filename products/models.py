from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

