from django import forms
from django.core.validators import RegexValidator
from django.utils.html import strip_tags


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120)
    company = forms.CharField(max_length=160)
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(
        max_length=32,
        validators=[
            RegexValidator(
                regex=r"^[0-9+().\s-]{6,32}$",
                message="Numéro de téléphone invalide.",
            )
        ],
    )
    message = forms.CharField(widget=forms.Textarea, max_length=4000)
    consent = forms.BooleanField()

    def _clean_text(self, value: str) -> str:
        value = (value or "").strip()
        value = strip_tags(value)
        return value

    def clean_name(self):
        return self._clean_text(self.cleaned_data.get("name"))

    def clean_company(self):
        return self._clean_text(self.cleaned_data.get("company"))

    def clean_phone(self):
        return (self.cleaned_data.get("phone") or "").strip()

    def clean_message(self):
        value = self._clean_text(self.cleaned_data.get("message"))
        value = value.replace("\r\n", "\n").replace("\r", "\n")
        return value