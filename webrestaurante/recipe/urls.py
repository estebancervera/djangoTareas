from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:recipe_id>/<slug:recipe_slug>/', views.recipe, name='recipe'),
]
