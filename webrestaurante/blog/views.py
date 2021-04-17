from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Category, Post

class BlogTemplateView(TemplateView):

    template_name = 'blog/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Post.objects.all()
        return context

# def blogs(request):
#      blogs = Post.objects.all()
     
#      return render(request, "blog/blog.html", {"blogs": blogs})

def category(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'blog/category.html', {"category": category})