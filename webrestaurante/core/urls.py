from django.urls import path
from . import views as core_views


urlpatterns = [
    path('', core_views.home, name='home'),
    path('history/', core_views.history, name='history'),
    path('store/', core_views.store, name='store'),
    path('contact/', core_views.contact, name='contact'),
    path('blog/', core_views.blog, name='blog'),
   
]