from django.db import models

# Create your models here.
class SanPham(models.Model):
    # Define your fields here
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as necessary

    def __str__(self):
        return self.name