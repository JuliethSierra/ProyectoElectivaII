# Create your models here.
from django.db import models
from db_conection import db

# Create your models here.
todo_coleccion = db['todo']

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
