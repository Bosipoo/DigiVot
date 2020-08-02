from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('digivotapp.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'DigiVot'
admin.site.index_title = 'Welcome Super Administrator'
admin.site.site_title = 'Control Panel'