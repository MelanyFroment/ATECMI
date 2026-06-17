import logging

from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .services.contact import send_contact_notification
from .services.contact_messages import save_contact_message

logger = logging.getLogger(__name__)

CONTACT_SUCCESS_MESSAGE = (
    "Merci, votre demande a bien été envoyée. "
    "Nous revenons vers vous sous 24–48h ouvrées."
)
CONTACT_SAVED_EMAIL_FAILED_MESSAGE = (
    "Votre demande a bien été enregistrée, mais l’envoi de l’e-mail de notification "
    "a échoué. Notre équipe sera informée via le backoffice."
)
CONTACT_INVALID_MESSAGE = (
    "Certaines informations sont invalides. Merci de vérifier le formulaire."
)


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            save_contact_message(request, cleaned)

            try:
                send_contact_notification(cleaned)
            except ImproperlyConfigured:
                logger.exception("Contact email misconfigured")
                messages.warning(request, CONTACT_SAVED_EMAIL_FAILED_MESSAGE)
            except Exception:
                logger.exception("Contact email delivery failed")
                messages.warning(request, CONTACT_SAVED_EMAIL_FAILED_MESSAGE)
            else:
                messages.success(request, CONTACT_SUCCESS_MESSAGE)

            return redirect(reverse("core:contact"))

        messages.error(request, CONTACT_INVALID_MESSAGE)
    else:
        form = ContactForm()

    return render(request, "core/contact.html", {"form": form})


def expertises(request):
    return render(request, "core/expertises.html")


def mentions_legales(request):
    return render(request, "core/mentions_legales.html")


def politique_confidentialite(request):
    return render(request, "core/politique_confidentialite.html")


def rse(request):
    return render(request, "core/rse.html")
