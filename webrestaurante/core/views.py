from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def history(request):
    return render(request, 'core/history.html')


def services(request):
    return render(request, 'core/services.html')


def store(request):
    return render(request, 'core/store.html')

def blog(request):
    return render(request, 'core/blog.html')
