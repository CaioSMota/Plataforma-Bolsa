"""brascch URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

#teste novo
urlpatterns = [
    # url padrão 
    path('', include('website.urls')),

    # interface administrativa 
    path('admin/', admin.site.urls),
]
