from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Inventory(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    value = models.PositiveBigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        # Calculate value as quantity * price
        self.value = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']