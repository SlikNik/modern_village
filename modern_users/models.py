from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


class ModernUsers(AbstractUser):
    user_pic= models.ImageField(blank=True, null=True)
    # user_pic= models.ImageField(upload_to=upload_image, default='modern_users/pics/already.png')
    age = models.IntegerField()
    birthday = models.DateField()
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=80)
    zipcode = models.CharField(max_length=10)
    phone = models.BigIntegerField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank = True, related_name="following", default=0)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'address', 'city', 'zipcode', 'age', 'birthday']

    def __str__(self):
        return self.username

    def upload_image(self, filename):
        return 'static/images/{}/{}'.format(self.username, filename)