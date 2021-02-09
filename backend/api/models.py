from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=400)
    complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
