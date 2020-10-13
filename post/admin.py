from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from post.models import Post

admin.site.register(Post, DraggableMPTTAdmin)
