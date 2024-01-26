from django.contrib import admin

# Register your models here.
from .models import Catagory, Artical

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_homepage', 'layout','ordering')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['status','is_homepage', 'layout',] # tao chuc nang fillter
    search_fields = ['name'] # tao chuc nang search
    class Media:
        js = ('my_admin/js/slugify.min.js','my_admin/js/jquery-3.6.0.min.js','my_admin/js/general.js') #tao auto slug bang tieng Viet

class ArticalAdmin(admin.ModelAdmin):
    list_display = ('name','status','ordering')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['status'] # tao chuc nang fillter
    search_fields = ['name'] # tao chuc nang search
    class Media:
        js = ('my_admin/js/slugify.min.js','my_admin/js/jquery-3.6.0.min.js','my_admin/js/general.js') #tao auto slug bang tieng Viet
   

admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Artical,ArticalAdmin)


