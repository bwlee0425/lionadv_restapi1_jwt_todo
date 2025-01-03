# todos/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='todos'
    )

    def __str__(self):
        return self.title
    
# pip install django djangorestframework djangorestframework-simplejwt django-cors-headers