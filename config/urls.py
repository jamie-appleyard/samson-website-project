from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #Django Admin
    path('ops-control/', admin.site.urls),

    #User Management
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    #Local Apps
    path('', include('pages.urls')),
    path('careers/', include('careers.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('news/', include('news.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
