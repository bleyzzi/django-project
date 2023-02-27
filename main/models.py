from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Task(models.Model):
    title = models.CharField('Name', max_length=100)
    task = models.TextField('Description')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'