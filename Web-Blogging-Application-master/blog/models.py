from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now) # Use auto_now=True for modifying date every time the post is updated(better for a field like last_modified).auto_now_add=True for seeting immutable date_created field.
    author = models.ForeignKey(User, on_delete= models.CASCADE) # User is the related table. CASCADE=deleting post when user is deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self): # After a new post is created, django doesn't know where to redirect. This function will provide a path to solve that issue.
        return reverse('post-detail', kwargs = {'pk': self.pk})      