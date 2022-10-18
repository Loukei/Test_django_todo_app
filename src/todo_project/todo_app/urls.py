from django.urls import path
from .views import TodoListListView, TodoItemListView

urlpatterns = [
    path('', TodoListListView.as_view(), name='index'),
    path('list/<int:listid>/', TodoItemListView.as_view(), name='list'),
]
