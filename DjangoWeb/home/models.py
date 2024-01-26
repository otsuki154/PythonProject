from django.db import models


from tinymce.models import HTMLField
from .helpers import *

# Create your models here.
class Catagory(models.Model):
    LAYOUT_CHOICE = (
        ('list','List'),
        ('grid', 'Grid')
    )
    STATUS_CHOICE = (
        ('draft','Draft'),
        ('published', 'Published')
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = models.BooleanField(default=False)
    layout = models.CharField(max_length=10,choices=LAYOUT_CHOICE, default="list")
    status = models.CharField(max_length=10,choices=STATUS_CHOICE, default="draft")
    ordering = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
class Artical(models.Model):
    LAYOUT_CHOICE = (
        ('list','List'),
        ('grid', 'Grid')
    )
    STATUS_CHOICE = (
        ('draft','Draft'),
        ('published', 'Published')
    )



    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10,choices=STATUS_CHOICE, default="draft")
    ordering = models.IntegerField(default=0)
    special = models.BooleanField(default=False)
    publish_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path,null=True,blank=True,verbose_name=(u'Contact list'))
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name