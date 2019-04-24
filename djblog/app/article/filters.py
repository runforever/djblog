import django_filters

from .models import Article


class ArticleFilter(django_filters.FilterSet):

    class Meta:
        model = Article
        fields = {
            'category': ['exact'],
            'created_at': ['year', 'month'],
            'title': ['icontains'],
        }
