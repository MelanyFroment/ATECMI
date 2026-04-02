from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def depalettisation(request):
    return render(request, 'core/depalettisation.html')

def paletisation(request):
    return render(request, 'core/paletisation.html')