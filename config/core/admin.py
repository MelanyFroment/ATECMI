from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "company", "name", "email", "consent")
    list_filter = ("consent", "created_at")
    search_fields = ("name", "company", "email", "phone", "message")
    readonly_fields = (
        "created_at",
        "name",
        "company",
        "email",
        "phone",
        "message",
        "consent",
        "ip_address",
        "user_agent",
    )

    def has_module_permission(self, request):
        return bool(request.user and request.user.is_active and request.user.is_superuser)

    def has_view_permission(self, request, obj=None):
        return bool(request.user and request.user.is_active and request.user.is_superuser)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return bool(request.user and request.user.is_active and request.user.is_superuser)
