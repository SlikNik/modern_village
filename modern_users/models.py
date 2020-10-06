from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class ModernUsers(AbstractUser):
    age = models.IntegerField()
    birthday = models.DateField()
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=10)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'address', 'city', 'zipcode', 'age', 'birthday']

    def __str__(self):
        return self.username
