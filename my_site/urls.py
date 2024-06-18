"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # urls that start with https://localhost:8000/
    # path('blog/', include('blog.urls')), # urls that start with https://localhost:8000/blog/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Django does not serve static files by default, because of security reasons, so you have to explicitly tell it to do so. + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# This is making django serve media files that are uploaded by users and not in the static folder
# We are exposing all the files stored in MEDIA_ROOT using the MEDIA_URL
