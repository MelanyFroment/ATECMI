import logging

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def resolve_from_email() -> str:
    if settings.EMAIL_HOST_USER:
        return settings.EMAIL_HOST_USER.strip()
    return (settings.DEFAULT_FROM_EMAIL or "").strip()


def build_contact_email_subject(cleaned_data: dict) -> str:
    company = (cleaned_data.get("company") or "").strip()
    name = (cleaned_data.get("name") or "").strip()
    label = company or name or "Contact"
    return f"[ATECMI] Nouvelle demande de contact — {label}"


def build_contact_email_body(cleaned_data: dict) -> str:
    return "\n".join(
        [
            "Nouvelle demande depuis le formulaire de contact ATECMI",
            "",
            f"Nom: {cleaned_data.get('name', '')}",
            f"Société: {cleaned_data.get('company', '')}",
            f"Email: {cleaned_data.get('email', '')}",
            f"Téléphone: {cleaned_data.get('phone', '')}",
            "",
            "Message:",
            f"{cleaned_data.get('message', '')}",
            "",
            f"Consentement: {'Oui' if cleaned_data.get('consent') else 'Non'}",
        ]
    )


def send_contact_notification(cleaned_data: dict) -> None:
    from_email = resolve_from_email()
    if not from_email:
        raise ImproperlyConfigured(
            "Aucun expéditeur e-mail configuré (EMAIL_HOST_USER ou DEFAULT_FROM_EMAIL)."
        )

    send_mail(
        subject=build_contact_email_subject(cleaned_data),
        message=build_contact_email_body(cleaned_data),
        from_email=from_email,
        recipient_list=[settings.CONTACT_RECIPIENT_EMAIL],
        fail_silently=False,
    )
    logger.info(
        "Contact notification sent from %s to %s",
        from_email,
        settings.CONTACT_RECIPIENT_EMAIL,
    )
