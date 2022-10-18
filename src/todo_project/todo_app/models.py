from enum import unique
from turtle import title
from django.db import models
from django.urls import reverse
from django.utils import timezone

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7.0)

# Create your models here.
class TodoList(models):
    """
    A todolist model to store the todoitem
    This is a personal TodoList app, which means no authentication required.

    title: each title is unique and limited size 100 
    """
    title = models.CharField(max_length = 200, unique=True)

    def get_absolute_url(self):
        return reverse('list', args=[self.id])

    def __str__(self):
        return self.title

class TodoItem(models):
    """A todo item is a simple and actionable steps. ex: wash dishses
    """
    title = models.CharField(max_length = 100)
    describtion = models.CharField(null = True, blank = True)
    create_date = models.DateTimeField(auto_now_add = True)
    due_date = models.DateTimeField(default = one_week_hence)
    todo_list = models.ForeignKey(TodoList, on_delete = models.CASCADE)

    class Meta:
        ordering = ["due_date"]
    
    def get_absolute_url(self):
        return reverse('todo', args=[self.id])
    
    def __str__(self):
        return self.title
