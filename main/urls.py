
from django.contrib import admin
from django.urls import path


from django.urls import path
from django.conf import settings

urlpatterns = [

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)