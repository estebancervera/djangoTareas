from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe
from django.views.generic import ListView
from django.views.generic import DetailView

# Create your views here.


# def recipes(request):
#     recipes = get_list_or_404(Recipe)
#     return render(request, 'recipe/recipes.html', {'recipes': recipes})

class RecipesListView(ListView):
   model = Recipe



# def recipe(request, recipe_id, recipe_slug):
#     recipe = get_object_or_404(Recipe, id=recipe_id)
#     return render(request, 'recipe/recipe.html', {'recipe': recipe})

class RecipeDetailView(DetailView):
   model= Recipe
