from django.urls import path
from . import views
from .views import RecipesListView, RecipeDetailView


urlpatterns = [
    path('', RecipesListView.as_view(), name='recipes'),
    path('<int:pk>/<slug:recipe_slug>/', RecipeDetailView.as_view(), name='recipe'),
]
