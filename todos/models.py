from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    isCompleted = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True)
    priority = models.IntegerField(default=-1)
