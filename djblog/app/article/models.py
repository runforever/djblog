from django.db import models

class Article(models.Model):
    """
    文章
    """

    title = models.CharField(
        '标题',
        max_length=50,
    )
    content = models.TextField(
        '内容',
    )
    author = models.ForeignKey(
        'auth.User',
        verbose_name='作者',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'article.Category',
        verbose_name='分类',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    created_at = models.DateTimeField(
        '创建时间',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        '更新时间',
        auto_now=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Category(models.Model):
    """
    文章分类
    """

    name = models.CharField(
        '分类名',
        max_length=50,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
