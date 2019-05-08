from django.shortcuts import render
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


class ArticleTagMixin(object):

    def get_tags(self):
        return Tag.objects.all()


class BlogIndexView(View, ArticleTagMixin):

    def get(self, request, *args, **kwargs):
        article_list = ArticleFilter(request.GET, queryset=Article.objects.all()).qs
        category_list = Category.objects.all()
        tag_list = self.get_tags()

        return render(
            request,
            'article/index.html',
            {
                'article_list': article_list,
                'category_list': category_list,
                'tag_list': tag_list,
            }
        )


class ArticleDetailView(DetailView, ArticleTagMixin):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = self.get_tags()
        return context
