from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    blogger = models.ForeignKey('Blogger', on_delete=models.RESTRICT, null=True)

    content = models.TextField(max_length=2000, help_text='Enter content of the blog')
    post_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.id)])
    class Meta:
        ordering = ['-post_date']
        permissions = [("can_mark_returned", "Set blog as returned")]

class Blogger(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField(max_length=1000, help_text='Enter a brief biography of the blogger')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("blogger_detail", args=[str(self.id)])
from django.contrib.auth.models import User
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Description')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
    
    
    