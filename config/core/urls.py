from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('depalettisation/', views.depalettisation, name='depalettisation'),
    path('palettisation/', views.palettisation, name='palettisation'),
]