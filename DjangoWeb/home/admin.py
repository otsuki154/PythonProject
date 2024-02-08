from django.contrib import admin

# Register your models here.
from .models import Catagory, Artical, Feed


from .define import *

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name','status','is_homepage', 'layout','ordering')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['status','is_homepage', 'layout',] # tao chuc nang fillter
    search_fields = ['name'] # tao chuc nang search
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS

class ArticalAdmin(admin.ModelAdmin):
    list_display = ('name','catagory','status','ordering','special')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['catagory','status','special'] # tao chuc nang fillter
    search_fields = ['name'] # tao chuc nang search
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS
   
class FeedAdmin(admin.ModelAdmin):
    list_display = ('name','status','ordering')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ['status'] # tao chuc nang fillter
    search_fields = ['name'] # tao chuc nang search
    class Media:
        js = ADMIN_SRC_JS
        css = ADMIN_SRC_CSS
   

admin.site.register(Catagory,CatagoryAdmin) #Thêm vào site admin
admin.site.register(Artical,ArticalAdmin)  #Thêm vào site admin
admin.site.register(Feed,FeedAdmin) #Thêm vào site admin

admin.site.site_header = ADMIN_SITE_NAME #Đặt lại tên cho site admin


