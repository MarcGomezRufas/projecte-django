from django.contrib import admin
from .models import Post, Autors, Tag
# Register your models here.

admin.site.register(Post)
admin.site.register(Autors)
admin.site.register(Tag)