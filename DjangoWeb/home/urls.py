from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name = "index"),
    
    # path('category/<slug:catagory_slug>', views.category, name = "catagory"),
    # path('artical/<slug:artical_slug>', views.artical, name = "artical"),
    path('<slug:feed_slug>.html', views.feed, name = "feed"),
    path('search.html', views.search, name = "search"),
    path('contact.html', views.contact, name = "contact"),
    path('about.html', views.about, name = "about"),

    path('<slug:catagory_slug>.html', views.category, name = "catagory"),
    # re_path(r'^tin-tong-hop-(?P<feed_slug>[\w-]+)\.html$', views.feed, name='feed'),
    re_path(r'^(?P<artical_slug>[\w-]+)-a(?P<artical_id>\d+)\.html$', views.artical, name='artical'),
    # re.search(r'^(?P<artical_slug>[\w-]+)-a\d+\.html$', last_path),


    path('tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
