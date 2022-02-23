from django.conf import settings
from django.db import models

STATUS_CHOICES = (
    ("IS", "In stock"),
    ("OS", "Out of stock"),
)


class Product(models.Model):
    title = models.CharField(max_length=200)
    cost = models.IntegerField()
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="IS"
    )

    def __str__(self):
        return f"{self.title} - {self.cost}"


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()
