from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CKEditor5Storage(FileSystemStorage):
    def __init__(self):
        super().__init__(
            location=settings.MEDIA_ROOT / "uploads",
            base_url=f"{settings.MEDIA_URL.rstrip('/')}/uploads/",
        )
