from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150] + "..."


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Article', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username