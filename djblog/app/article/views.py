from django.shortcuts import render, get_object_or_404

from django.views.generic.detail import DetailView
from django.views import View

from .filters import (
    ArticleFilter,
)
from .models import (
    Article,
    Category,
    Tag,
)


class BlogIndexView(View):

    def get(self, request, *args, **kwargs):
        article_list = ArticleFilter(request.GET, queryset=Article.objects.all()).qs
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()

        return render(
            request,
            'article/index.html',
            {
                'article_list': article_list,
                'category_list': category_list,
                'tag_list': tag_list,
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
"""


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        return context
