from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from post.models import Post

admin.site.register(Post, DraggableMPTTAdmin)
