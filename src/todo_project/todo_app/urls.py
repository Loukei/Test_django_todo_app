from django.urls import path
from .views import TodoListListView

urlpatterns = [
    path('', TodoListListView.as_view(), name='index'),
    # path(''),
]
