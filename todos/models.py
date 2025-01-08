# todos/models.py
from django.db import models
from django.conf import settings
<<<<<<< HEAD
from django.contrib.auth.models import User
=======

>>>>>>> fcba87d9aba674431dd54ea4b932190fa2b6c000
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