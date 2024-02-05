from .models import Catagory,Feed,Artical
from django.utils import timezone
from .define import *
from django.db.models import Count

def items_catagory_sidebar_menu(request):
    items_catagory_sidebar_menu = Catagory.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE ).order_by("ordering").annotate(num_artical=Count('artical'))[:APP_VALUE_CATAGORY_NUM_MENU_SIDEBAR_DEFINE]
    return {"items_catagory_sidebar_menu":items_catagory_sidebar_menu}

def items_feed_sidebar_menu(request):
    items_feed_sidebar_menu = Feed.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE ).order_by("ordering")[:APP_VALUE_FEED_NUM_MENU_SIDEBAR_DEFINE]
    return {"items_feed_sidebar_menu":items_feed_sidebar_menu}

def items_feed_sidebar_recent(request):
    skip_slug = request.get_full_path().replace("/artical/","")
    items_feed_sidebar_recent = Artical.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE , publish_date__lte = timezone.now()).order_by("-publish_date").exclude(slug=skip_slug)[:APP_VALUE_FEED_NUM_RECENT_SIDEBAR_DEFINE]
    
    return {"items_feed_sidebar_recent":items_feed_sidebar_recent}

def items_feed_sidebar_random(request):
    skip_slug = request.get_full_path().replace("/artical/","")
    items_feed_sidebar_random = Artical.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE , publish_date__lte = timezone.now()).order_by("?").exclude(slug=skip_slug)[:APP_VALUE_FEED_NUM_RANDOM_FOOTER_DEFINE]
    
    return {"items_feed_sidebar_random":items_feed_sidebar_random,
            "img_src":APP_VALUE_DÈAULT_IMG_DEFINE}

def items_feed_sidebar_trending(request):
    skip_slug = request.get_full_path().replace("/artical/","")
    items_feed_sidebar_trending = Artical.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE , publish_date__lte = timezone.now()).order_by("?").exclude(slug=skip_slug)[:APP_VALUE_FEED_NUM_TRENDING_FOOTER_DEFINE]
    
    return {"items_feed_sidebar_trending":items_feed_sidebar_trending}