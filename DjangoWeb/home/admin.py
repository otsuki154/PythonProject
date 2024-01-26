from django.contrib import admin

# Register your models here.
from .models import Catagory

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_homepage', 'layout','ordering')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Catagory,CatagoryAdmin)


