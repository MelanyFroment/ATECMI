from django.urls import path

from . import views

app_name = "solutions"

urlpatterns = [
    path("depalettisation-industrielle/", views.depalettisation, name="depalettisation"),
    path("palettisation-robotisee/", views.palettisation, name="palettisation"), 
    path("convoyage-produit/", views.convoyage_produit, name="convoyage_produit"),
    path("encartonnage/", views.encartonnage, name="encartonnage"),
    path("convoyage-colis/", views.convoyage_colis, name="convoyage_colis"),
    path("integration/", views.integration, name="integration"),
    path("convoyage-palette/", views.convoyage_palette, name="convoyage_palette"),
    path("solutions-robotisees/", views.solutions_robotisees, name="solutions_robotisees"),
]


