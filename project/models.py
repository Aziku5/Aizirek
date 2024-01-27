from django.db import models


class Task(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.CharField(default=False)
    created = models.CharField(auto_created=True)
