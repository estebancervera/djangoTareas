from django.shortcuts import render

# Create your views here.
from .models import Category, Post
# Create your views here.

def blogs(request):
     blogs = Post.objects.all()
     
     return render(request, "blog/blog.html", {"blogs": blogs})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'blog/category.html', {"category": category})