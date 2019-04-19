from django.shortcuts import render
from django.views import View

from .models import Article


class ArticleListView(View):

    def get(self, request, *args, **kwargs):
        article_list = Article.objects.all()
        return render(request, 'article/list.html', {'article_list': article_list})
