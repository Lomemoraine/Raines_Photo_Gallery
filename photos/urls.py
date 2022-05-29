from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery-home'),
    # path(r'^search/',views.search_results, name='search_results'),
    # re_path(r'^category/(\w+)', views.get_category,name='get_category'),
    # re_path(r'^location/(\w+)', views.get_location,name='get_location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)