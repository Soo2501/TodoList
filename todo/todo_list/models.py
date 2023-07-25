from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

    class meta:
        ordering = ['completed']