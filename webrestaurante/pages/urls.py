from django.urls import path
from . import views as page_views

urlpatterns = [
    path('<int:page_id>', page_views.page, name='page'),
]