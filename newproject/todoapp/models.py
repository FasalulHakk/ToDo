from django.db import models

# Create your models here.
class tasks(models.Model):
    task=models.CharField(max_length=200)
    priority=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.task

