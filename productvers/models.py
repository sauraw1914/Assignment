from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    weight = models.FloatField(max_length=255, null=True)
    price = models.FloatField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name