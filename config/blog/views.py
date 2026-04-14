from django.shortcuts import get_object_or_404, render

from .models import Article


def article_list(request):
    articles = Article.objects.order_by("-created_at")
    return render(request, "blog/article_list.html", {"articles": articles})


def article_detail(request, slug: str):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/article_detail.html", {"article": article})
