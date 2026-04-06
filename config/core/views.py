from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def depalettisation(request):
    return render(request, 'core/depalettisation.html')

def palettisation(request):
    return render(request, 'core/palettisation.html')

def convoyage_produit(request):
    return render(request, "core/convoyage-produit.html")

def encartonnage(request):
    return render(request, "core/encartonnage.html")

def convoyage_colis(request):
    return render(request, "core/convoyage-colis.html")

def integration(request):
    return render(request, "core/integration.html")