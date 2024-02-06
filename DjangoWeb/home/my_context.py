from .models import Catagory,Feed,Artical
from django.utils import timezone
from .define import *
from .helpers import *
from django.db.models import Count
import requests
import json

def items_catagory_sidebar_menu(request):
    items_catagory_sidebar_menu = Catagory.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE ).order_by("ordering").annotate(num_artical=Count('artical'))[:APP_VALUE_CATAGORY_NUM_MENU_SIDEBAR_DEFINE]
    return {
        "items_catagory_sidebar_menu":items_catagory_sidebar_menu,
            "logo_image":APP_VALUE_LOGO_IMG_DEFINE,
            "img_src":APP_VALUE_DEFAULT_IMG_DEFINE
            }



def items_feed_sidebar_menu(request):
    items_feed_sidebar_menu = Feed.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE ).order_by("ordering")[:APP_VALUE_FEED_NUM_MENU_SIDEBAR_DEFINE]
    return {"items_feed_sidebar_menu":items_feed_sidebar_menu}



def items_feed_sidebar_recent(request):
    skip_slug = get_skip_slug_artical(request.path)
    items_feed_sidebar_recent = Artical.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE , publish_date__lte = timezone.now()).order_by("-publish_date").exclude(slug=skip_slug)[:APP_VALUE_FEED_NUM_RECENT_SIDEBAR_DEFINE]
    
    return {"items_feed_sidebar_recent":items_feed_sidebar_recent}



def items_feed_sidebar_random(request):
    skip_slug = get_skip_slug_artical(request.path)
    items_feed_sidebar_random = Artical.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE , publish_date__lte = timezone.now()).order_by("?").exclude(slug=skip_slug)[:APP_VALUE_FEED_NUM_RANDOM_FOOTER_DEFINE]
    
    return {"items_feed_sidebar_random":items_feed_sidebar_random,
            "img_src":APP_VALUE_DEFAULT_IMG_DEFINE}



def items_feed_sidebar_trending(request):
    skip_slug = get_skip_slug_artical(request.path)
    items_feed_sidebar_trending = Artical.objects.filter(status=APP_VALUE_STATUS_ACTIVE_DEFINE , publish_date__lte = timezone.now()).order_by("?").exclude(slug=skip_slug)[:APP_VALUE_FEED_NUM_TRENDING_FOOTER_DEFINE]
    
    return {"items_feed_sidebar_trending":items_feed_sidebar_trending}



def items_price_sidebar_coin(request):

    items_price_sidebar_coin = []
    response = requests.get(APP_VALUE_COIN_URL_SIDEBAR_DEFINE)
    if response.status_code == 200:
        data = response.json()[:APP_VALUE_COIN_NUM_SIDEBAR_DEFINE]
        items_price_sidebar_coin = [item for item in data if item["name"] not in APP_VALUE_COIN_EXCLUDE_SIDEBAR_DEFINE ]
    
    return {
        "items_price_sidebar_coin":items_price_sidebar_coin,
            }



def items_price_sidebar_gold(request):

    items_price_sidebar_gold = []
    response = requests.get(APP_VALUE_GOLD_URL_SIDEBAR_DEFINE)
    if response.status_code == 200:
        items_price_sidebar_gold = response.json()[:APP_VALUE_GOLD_NUM_SIDEBAR_DEFINE]
    
    return {
        "items_price_sidebar_gold":items_price_sidebar_gold,
            }