from django.urls import path
from . import views as blog_views
from .views import BlogTemplateView, BlogCategoryTemplateView

urlpatterns = [
    path('', BlogTemplateView.as_view(), name="blog"),
    path('category/<int:category_id>', BlogCategoryTemplateView.as_view(), name='category'),
]