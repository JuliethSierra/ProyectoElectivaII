# Create your models here.
from djongo import models
from db_conection import db

# Create your models here.
todo_coleccion = db['todo']


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

