from django.contrib import admin

# Register your models here.

from .models import Cocktail, Comment

admin.site.register(Cocktail)
admin.site.register(Comment)