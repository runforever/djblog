from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView

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


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
