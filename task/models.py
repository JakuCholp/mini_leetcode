from django.db import models
from user.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField(max_length=170)
    input = models.CharField(max_length=140)
    output = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class AllVariables(models.Model):
    variables = models.TextField()
    result = models.CharField(max_length=140)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)





