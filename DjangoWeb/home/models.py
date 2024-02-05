from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField
from .helpers import *
from .custom_field import *
from .define import *

# Create your models here.

class Catagory(models.Model):

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10,choices=APP_VALUE_LAYOUT_CHOICE, default=APP_VALUE_LAYOUT_DEFINE)
    status = models.CharField(max_length=10,choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFINE)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = TABLE_CATEGORY_SHOW #Đặt lại tên hiển thị

    def __str__(self) -> str:
        return self.name
    
class Artical(models.Model):

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10,choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFINE)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path,null=True,blank=True,verbose_name=(u'Contact list'))
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)

    class Meta:
            verbose_name_plural = TABLE_ARTICAL_SHOW #Đặt lại tên hiển thị

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("artical", kwargs={"artical_slug": self.slug})
    

class Feed(models.Model):

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10,choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFINE)
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = TABLE_FEED_SHOW #Đặt lại tên hiển thị

    def __str__(self) -> str:
        return self.name