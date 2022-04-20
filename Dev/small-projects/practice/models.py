# Create your models here.
# Projects
from django.db.models import BooleanField, ManyToManyField
from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class ProjectIdeas(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=1000, null=True)
    due_date = models.DateField()
    estimated_hours = models.DecimalField(max_digits=10, decimal_places=3, null=True)

    def __str__(self):
        return f'{self.title}'
