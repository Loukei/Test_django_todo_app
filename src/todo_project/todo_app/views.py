from typing import Type, Optional
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Model
from .models import TodoList, TodoItem

# Create your views here.
class TodoListListView(ListView):
    model: Optional[Type[Model]] = TodoList
    template_name: str = "todo_app/todolist.html" 
