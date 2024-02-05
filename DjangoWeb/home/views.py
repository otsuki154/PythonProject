from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Catagory, Artical
from .define import *
# Create your views here.

def index(request):

    items_artical_special = Artical.objects.filter(special=True, status="published", publish_date__lte = timezone.now()).order_by("-publish_date")[:5]
    items_catagory = Catagory.objects.filter(status="published", is_homepage = True).order_by("ordering")

    for catagory in items_catagory:
        catagory.artical_filter = catagory.artical_set.filter(status="published", publish_date__lte = timezone.now()).order_by("-publish_date")

    return render(request, 'pages/index.html',{
        "items_artical_special":items_artical_special,
        "items_catagory":items_catagory,
    })

def category(request,catagory_slug):
    # catagory_slug => thông tin catagory => artical thuộc catagoru -> đổ dữ liệu ra phía client
    #lấy thông tin catarory
    item_catagory = get_object_or_404(Catagory, slug=catagory_slug, status="published")
    #lấy artical thuộc catarory
    items_artical = Artical.objects.filter(catagory=item_catagory, status="published", publish_date__lte = timezone.now()).order_by("-publish_date")

    #phân trang
    paginator = Paginator(items_artical, APP_VALUE_ARTICAL_NUM_IN_PAGE_DEFINE)
    page = request.GET.get('page')

    items_artical = paginator.get_page(page)

    return render(request, 'pages/category.html',{
        "item_catagory":item_catagory,
        "items_artical":items_artical,
        "paginator":paginator,
    })

def artical(request,artical_slug):

      #lấy thông tin catarory
    item_artical = get_object_or_404(Artical, slug=artical_slug,status="published", publish_date__lte = timezone.now())
    items_artical_related = Artical.objects.filter(catagory=item_artical.catagory, status="published", publish_date__lte = timezone.now()).order_by("-publish_date").exclude(slug=artical_slug)[:APP_VALUE_ARTICAL_RELATED_MAX_DEFINE]

    return render(request, 'pages/artical.html',{
        "item_artical":item_artical,
        "items_artical_related":items_artical_related,
    })

def feed(request):
    return render(request, 'pages/feed.html',{})

def search(request):
    return render(request, 'pages/search.html',{})
