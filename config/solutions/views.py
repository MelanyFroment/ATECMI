from django.shortcuts import render


def depalettisation(request):
    return render(request, "solutions/depalettisation.html")


def palettisation(request):
    return render(request, "solutions/palettisation.html")


def convoyage_produit(request):
    return render(request, "solutions/convoyage-produit.html")


def encartonnage(request):
    return render(request, "solutions/encartonnage.html")


def convoyage_colis(request):
    return render(request, "solutions/convoyage-colis.html")


def integration(request):
    return render(request, "solutions/integration.html")


def convoyage_palette(request):
    return render(request, "solutions/convoyage-palette.html")


def solutions_robotisees(request):
    return render(request, "solutions/solutions-robotisees.html")
