from django.contrib import admin
from .models import Menu

# Register your models here.

class MenuChange(admin.ModelAdmin):
     list_display = ('name', 'price')

admin.site.register(Menu, MenuChange)


