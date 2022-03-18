from django.db import models

# Create your models here.
# Here I use the Model class to define the different columns included in the project table
# The left side of the "=" is the column name
# The right side of the "=" defines the data that can be included in the column
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=1000)