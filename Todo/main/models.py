from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):

    name = models.CharField(max_length=150)
    createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def getdesc(self):
        return self.description[:50] + '...'


class TodoItems(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True)
    Description = models.TextField(null=True, blank=True)
    iscompleted = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
