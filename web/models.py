from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class NewsTag(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post_date = models.DateField(verbose_name='Дата публикации', default=timezone.now)
    tags = models.ManyToManyField(NewsTag, verbose_name='Теги', blank=True)
    text = models.TextField(verbose_name='Текст новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class Comment(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст комментария')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
