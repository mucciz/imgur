from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^gallery',views.galleries,name = 'gallery'),
    url(r'^location',views.location,name = 'location'),
    url(r'^location/(?P<location>\d+)', views.search_by_location, name='location_filter'),
    url(r'^search/', views.search_results, name='search_results')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)