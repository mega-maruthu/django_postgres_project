
from django.db import models

# We are using Python Classes here (Python Basics)
class Task(models.Model):
    # These variables define the columns in your PostgreSQL table
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # This Python method tells Django how to print this object as text
    def __str__(self):
        return self.title