# Create your models here.
from django.db import models

class DisputeLetter(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    credit_bureau = models.CharField(max_length=255)
    generated_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
