import re

from django import template

register = template.Library()

_MEDIA_URL_PATTERN = re.compile(r"https?://[^/]+(/media/[^\"'\s>]+)")


@register.filter(is_safe=True)
def fix_media_urls(value: str) -> str:
    if not value:
        return value
    return _MEDIA_URL_PATTERN.sub(r"\1", value)
