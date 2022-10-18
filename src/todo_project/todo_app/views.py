from typing import Type, Optional, Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Model, QuerySet
from .models import TodoList, TodoItem

# Create your views here.
class TodoListListView(ListView):
    model: Optional[Type[Model]] = TodoList
    template_name: str = "todo_app/todolist.html" 

class TodoItemListView(ListView):
    model: Optional[Type[Model]] = TodoItem
    template_name: str = "todo_app\listitem.html"

    def get_queryset(self) -> QuerySet[Any]:
        "Override queryset function by set current list_id"
        return TodoItem.objects.filter(todo_list_id = self.kwargs["listid"])
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        "Override context_data function to add current todolist"
        context = super().get_context_data(**kwargs)
        context["todo_list"] = TodoList.objects.get(id = self.kwargs["listid"])
        return context