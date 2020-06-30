from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    author = models.ForeignKey(
        to='Author', on_delete=models.CASCADE,
        related_name="articles", null=True, blank=True
    )

    readers = models.ManyToManyField(to=User, related_name="articles", blank=True)
    publications_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    picture = models.ImageField(null=True, blank=True, upload_to='articles/' + datetime.today().strftime('%Y%m%d'))
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)
    tag = models.ManyToManyField('Tag', blank=True, related_name='article')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'статью'
        verbose_name_plural = 'статьи'


class Author(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='author_photo', null=True, blank=True)
    user = models.OneToOneField(
        to=User, on_delete=models.SET_NULL, related_name="author",
        null=True, blank=True
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Comment(models.Model):
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.user.username + " - " + self.text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
    
class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
