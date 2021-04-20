from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

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


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('recipes:recipes')

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
       return reverse_lazy('recipes:update', args=[self.object.id]) + '?ok'

