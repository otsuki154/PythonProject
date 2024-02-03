from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name = "index"),
    path('category/', views.category, name = "category"),
    path('artical/', views.artical, name = "artical"),
    path('feed/', views.feed, name = "feed"),
    path('search/', views.search, name = "search"),

    
    path('tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
