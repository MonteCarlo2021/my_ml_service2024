"""
# backend/server/server/urls.py file
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns
# Ersetzt wegen veralteter url()-Funktion in Django 4 (Chat GPT)
"""


from django.urls import path, include 
from django.contrib import admin

#from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/v1/', include('apps.endpoints.urls')),
]

#urlpatterns += endpoints_urlpatterns
