from django.db import models


# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=200, blank=True, default='')
    completed = models.BooleanField(default=False)


'''
In summary, this Todo model defines a database table with two fields: task and completed. 
Each instance of the Todo model represents a to-do item with a task description and a completion status.
Django will create the corresponding database table for this model when you run database migrations 
(python manage.py makemigrations and python manage.py migrate).
'''
