from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name = "index"),
    path('category/<slug:catagory_slug>', views.category, name = "catagory"),
    path('artical/<slug:artical_slug>', views.artical, name = "artical"),
    path('feed/<slug:feed_slug>', views.feed, name = "feed"),
    path('search/', views.search, name = "search"),
    path('contact/', views.contact, name = "contact"),
    path('about/', views.about, name = "about"),


    path('tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
