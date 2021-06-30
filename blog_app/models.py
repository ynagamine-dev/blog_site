from django.db import models
from django.utils import timezone


class Tag(models.Model):

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=30)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag, related_name='article_set', blank=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title
