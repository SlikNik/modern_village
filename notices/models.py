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
    post_date = models.DateTimeField(default=timezone.now)
    # notice_pic = models.ImageField(blank=True, null=True)
    # models.DateTimeField(auto_now=True)
    price = models.FloatField(blank=True, null=True)
    creator = models.ForeignKey(ModernUsers, on_delete=models.CASCADE)
    is_urgent = models.BooleanField()

    def __str__(self):
        return f'{self.type_of}-{self.title}'

    def upload_image(self, filename):
        return 'static/images/{}/{}'.format(self.title, filename)
