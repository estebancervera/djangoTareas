from django.urls import path
from . import views
from .views import RecipesListView, RecipeDetailView, RecipeCreateView, RecipeUpdateView


recipe_patterns = ([
    path('', RecipesListView.as_view(), name='recipes'),
    path('<int:pk>/<slug:recipe_slug>/', RecipeDetailView.as_view(), name='recipe'),
    path('create/', RecipeCreateView.as_view(), name='create'),
    path('update/<int:pk>', RecipeUpdateView.as_view(), name='update'),

],'recipes')
