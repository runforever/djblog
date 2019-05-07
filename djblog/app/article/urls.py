from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^index/$',
        views.BlogIndexView.as_view(),
        name='index'
    ),
    url(
        r'^detail/(?P<pk>\d+)/$',
        views.ArticleDetailView.as_view(),
        name='detail'
    ),
    url(
        r'^comment/$',
        views.CommentView.as_view(),
        name='comment'
    ),
]
