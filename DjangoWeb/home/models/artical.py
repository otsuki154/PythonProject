from django.db import models
from django.urls import reverse

from tinymce.models import HTMLField
from home.helpers import *
from home.custom_field import *
from home.define import *

from .catagory import Catagory

# Create your models here.

class Artical(models.Model):

    name = models.CharField(unique=True, max_length=500)
    slug = models.SlugField(unique=True, max_length=500)
    status = models.CharField(max_length=10,choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFINE)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path,max_length=500,null=True,blank=True,verbose_name=(u'Contact list'))
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = TABLE_ARTICAL_SHOW #Đặt lại tên hiển thị
        constraints = [
        models.UniqueConstraint(fields=['name', 'slug'], name='unique_name_slug_constraint')
        ]

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("artical", kwargs={"artical_slug": self.slug, 'artical_id':self.id})
    