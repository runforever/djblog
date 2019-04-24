from django.shortcuts import render, get_object_or_404
from django.views import View

from .filters import (
    ArticleFilter,
)
from .models import (
    Article,
    Category,
)


class BlogIndexView(View):

    def get(self, request, *args, **kwargs):
        article_list = ArticleFilter(request.GET, queryset=Article.objects.all()).qs
        category_list = Category.objects.all()

        return render(
            request,
            'article/index.html',
            {
                'article_list': article_list,
                'category_list': category_list,
            }
        )
"""


class BlogIndexView(View):

    def get(self, request, *args, **kwargs):
        article_list = Article.objects.all()
        category_list = Category.objects.all()

        article_list = ArticleFilter(request.GET, queryset=Article.objects.all())
        category_id = request.GET.get('category')
        try:
            category_id = int(category_id)
        except (ValueError, TypeError):
            category_id = None

        if category_id:
            article_list = article_list.filter(category_id=category_id)

        return render(
            request,
            'article/index.html',
            {
                'article_list': article_list,
                'category_list': category_list,
            }
        )
"""

class ArticleDetailView(View):

    def get(self, request, id, *args, **kwargs):
        article = get_object_or_404(Article, id=id)

        return render(
            request,
            'article/detail.html',
            {
                'article': article
            }
        )
