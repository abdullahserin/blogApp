from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=40)

    def _str_(self):
        return self.name

class Blog(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=40, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    category = models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)

    

class Likes(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')   # user, blog çifti like'lar içinde bir arada uniq olacak ali'nin sayılar isimli blogu bir defa like'lanabilir.

class PostViews(models.Model):
    user = models.ForeignKey(User, related_name='post_views', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='views', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
