from django.contrib import admin
from calculator.models import Data


# Register your models here.

from . import models

class DataAdmin(admin.ModelAdmin):
    search_fields = ['your_name', 'partner_name']
    list_display = ['your_name', 'partner_name']


admin.site.register(Data,DataAdmin)