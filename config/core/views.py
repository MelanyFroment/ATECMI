from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import ContactMessage

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            ContactMessage.objects.create(
                name=cleaned.get("name", ""),
                company=cleaned.get("company", ""),
                email=cleaned.get("email", ""),
                phone=cleaned.get("phone", ""),
                message=cleaned.get("message", ""),
                consent=bool(cleaned.get("consent")),
                ip_address=request.META.get("REMOTE_ADDR"),
                user_agent=(request.META.get("HTTP_USER_AGENT") or "")[:512],
            )
            subject = f"[ATECMI] Nouvelle demande de contact — {cleaned.get('company', '').strip() or cleaned.get('name', '')}"
            message = "\n".join(
                [
                    "Nouvelle demande depuis le formulaire de contact ATECMI",
                    "",
                    f"Nom: {cleaned.get('name', '')}",
                    f"Société: {cleaned.get('company', '')}",
                    f"Email: {cleaned.get('email', '')}",
                    f"Téléphone: {cleaned.get('phone', '')}",
                    "",
                    "Message:",
                    f"{cleaned.get('message', '')}",
                    "",
                    f"Consentement: {'Oui' if cleaned.get('consent') else 'Non'}",
                ]
            )

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=None,  # uses DEFAULT_FROM_EMAIL
                    recipient_list=["melany.from@yahoo.com"],
                )
            except Exception:
                messages.error(
                    request,
                    "Votre demande a bien été enregistrée, mais l’envoi email a échoué (configuration SMTP).",
                )
                return redirect(reverse("core:contact"))

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


def expertises(request):
    return render(request, "core/expertises.html")


def mentions_legales(request):
    return render(request, "core/mentions_legales.html")


def politique_confidentialite(request):
    return render(request, "core/politique_confidentialite.html")


def rse(request):
    return render(request, "core/rse.html")