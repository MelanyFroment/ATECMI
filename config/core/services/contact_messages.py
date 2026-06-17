from django.http import HttpRequest

from ..models import ContactMessage


def save_contact_message(request: HttpRequest, cleaned_data: dict) -> ContactMessage:
    return ContactMessage.objects.create(
        name=cleaned_data.get("name", ""),
        company=cleaned_data.get("company", ""),
        email=cleaned_data.get("email", ""),
        phone=cleaned_data.get("phone", ""),
        message=cleaned_data.get("message", ""),
        consent=bool(cleaned_data.get("consent")),
        ip_address=get_client_ip(request),
        user_agent=(request.META.get("HTTP_USER_AGENT") or "")[:512],
    )


def get_client_ip(request: HttpRequest) -> str | None:
    forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")
