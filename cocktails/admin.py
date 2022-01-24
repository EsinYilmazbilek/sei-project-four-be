from django.contrib import admin

# Register your models here.

from .models import Cocktail, Comment, Save

admin.site.register(Cocktail)
admin.site.register(Comment)
admin.site.register(Save)
