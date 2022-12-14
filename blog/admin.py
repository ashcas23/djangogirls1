from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Image


class postadmin (admin.ModelAdmin):
    filter_horizontal = ["images"]
admin.site.register(Post,postadmin)
admin.site.register(Image)
