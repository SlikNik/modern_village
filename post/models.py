from django.db import models
from django.utils import timezone
from modern_users.models import ModernUsers
from mptt.models import MPTTModel, TreeForeignKey


class Post(MPTTModel):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(ModernUsers, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            blank=True, null=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['post_date']

    def __str__(self):
        return self.title
