from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import (
    Article,
)


class BlogIndexView(View):

    def get(self, request, *args, **kwargs):
        article_list = Article.objects.all()

        return render(
            request,
            'article/index.html',
            {
                'article_list': article_list,
            }
        )


class ArticleDetailView(View):

    def get(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, id=pk)

        return render(
            request,
            'article/detail.html',
            {
                'article': article
            }
        )
