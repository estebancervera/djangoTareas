from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
from .models import Service
# Create your views here.

# def services(request):
#     # html = html_base + """
        
#     # """
#     # return HttpResponse(html)
#      services = Service.objects.all()
#      return render(request, "services/services.html", {"services": services})




class ServiceTemplateView(TemplateView):

    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context
        