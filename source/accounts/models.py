from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)



class Stores(models.Model):
    store_name = models.CharField(max_length=200)
    open_hours = models.CharField(max_length=10)
    store_rating = models.CharField(max_length=5)

