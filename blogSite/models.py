from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField()

    def published(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        self.comments.filter(approved_comments=True)
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comments(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    post = models.ForeignKey('blogSite.Post', related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.text
