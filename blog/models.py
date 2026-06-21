from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import uuid # Required for unique book instances


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null= True)
    

    class Meta:    
        ordering = ['username']    

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.username
        
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='posts')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='comments')
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    published_date = models.DateTimeField(auto_now_add=True)    

    class Meta:
        ordering = ['-published_date']    
    
    def __str__(self):
        return f'{self.post} by {self.author}'