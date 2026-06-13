from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("expertises/", views.expertises, name="expertises"),
    path("mentions-legales/", views.mentions_legales, name="mentions_legales"),
    path(
        "politique-confidentialite/",
        views.politique_confidentialite,
        name="politique_confidentialite",
    ),
    path("demarche-rse/", views.rse, name="rse"),
]