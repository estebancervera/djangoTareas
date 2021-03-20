from django.shortcuts import render

# Create your views here.
from .models import Category, Post
# Create your views here.

def blogs(request):
    # html = html_base + """
        
    # """
    # return HttpResponse(html)
     blogs = Post.objects.all()
     print("LOL")
     
     return render(request, "blog/blog.html", {"blogs": blogs})