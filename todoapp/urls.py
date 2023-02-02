from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name="home"),
    path('todos/', views.todoList, name='TodoList'),
    path('todo/<str:pk>/', views.todoListDetails, name='TodoListDetails'),
    path('todo-create/', views.todoCreate, name='TodoCreate'),
    path('todo-update/<str:pk>/', views.todoUpdate, name='TodoUpdate'),
    path('todo-delete/<str:pk>/', views.todoDelete, name='todoDelete'),
]
