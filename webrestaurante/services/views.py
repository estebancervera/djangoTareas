from django.shortcuts import render

# Create your views here.
from .models import Service
# Create your views here.

def services(request):
    # html = html_base + """
        
    # """
    # return HttpResponse(html)
     services = Service.objects.all()
     return render(request, "services/services.html", {"services": services})