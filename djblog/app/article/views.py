from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views import View

from .filters import (
    ArticleFilter,
)
from .models import (
    Article,
    Category,
    Tag,
    Comment,
)
from .forms import (
    CommentForm
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


class CommentView(View):

    def post(self, request, **kwargs):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save()
            return redirect('detail', pk=comment.article_id)

        return HttpResponse(form.errors)
"""


class ArticleDetailView(DetailView, ArticleTagMixin):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = self.get_tags()
        context['comment_list'] = Comment.objects.filter(article=context['article'])
        return context


class CommentView(CreateView):

    model = Comment
    fields = (
        'article',
        'nickname',
        'email',
        'content',
    )
    success_url = 'detail'

    def form_valid(self, form):
        super().form_valid(form)
        return redirect('detail', pk=form.data['article'])

    def form_invalid(self, form):
        super().form_invalid(form)
        return HttpResponse('表单有误请返回重新填写')
