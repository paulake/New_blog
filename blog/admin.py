from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'author')

admin.site.register(Post, PostAdmin)
