from django.db import models
from django.utils import timezone
from modern_users.models import ModernUsers

class Notice (models.Model):
    class TypeOf(models.TextChoices):
        NEWS = 'NEWS'
        TRAFFIC = 'TRAFFIC'
        ALERT = 'ALERT'
        EVENT = 'EVENT'
        OTHER = 'OTHER'
    type_of = models.CharField(
        max_length=200, 
        choices=TypeOf.choices,
        default=TypeOf.NEWS)
    title = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0.00)
    # expire_date = models.DateField()
    creator = models.ForeignKey(ModernUsers, on_delete=models.CASCADE)
    is_urgent = models.BooleanField()

    def __str__(self):
        return f'{self.type_of}-{self.title}'

    # @property
    # def expire_date(self):
    #     if self.is_urgent:
    #         return 