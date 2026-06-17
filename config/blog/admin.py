from django.contrib import admin
from django.utils.text import slugify

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "slug", "content")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
    date_hierarchy = "created_at"

    fieldsets = (
        (
            None,
            {
                "fields": ("title", "slug", "image", "content"),
            },
        ),
        (
            "Publication",
            {
                "fields": ("created_at",),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            base_slug = slugify(obj.title) or "article"
            slug = base_slug
            counter = 1
            while Article.objects.filter(slug=slug).exclude(pk=obj.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            obj.slug = slug
        super().save_model(request, obj, form, change)
