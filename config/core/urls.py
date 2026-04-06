from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('depalettisation/', views.depalettisation, name='depalettisation'),
    path('palettisation/', views.palettisation, name='palettisation'),
    path('convoyage-produit/', views.convoyage_produit, name='convoyage_produit'),
    path('encartonnage/', views.encartonnage, name='encartonnage'),
    path('convoyage-colis/', views.convoyage_colis, name='convoyage_colis'),
    path('integration/', views.integration, name='integration'),
]