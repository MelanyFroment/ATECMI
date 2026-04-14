from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "Merci, votre demande a bien été envoyée. Nous revenons vers vous sous 24–48h ouvrées.",
            )
            return redirect(reverse("core:contact"))

        messages.error(
            request,
            "Certaines informations sont invalides. Merci de vérifier le formulaire.",
        )
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})