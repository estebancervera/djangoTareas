from django.urls import path

from .views import ServiceTemplateView

urlpatterns = [
    path('', ServiceTemplateView.as_view(), name='services'),
]