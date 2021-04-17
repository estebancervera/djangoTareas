"""webrestaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from services import views as views_services
from django.conf import settings

urlpatterns = [
    path('services/', include('services.urls')),
    path('page/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('recipe/', include('recipe.urls')),
    path('', include('core.urls')),
    # path('services/', views_services.services, name="services"),
   
]

if settings.DEBUG:
        from django.conf.urls.static import static
        urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#         from django.conf.urls.static import static
#         urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)