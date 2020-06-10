from . import views
from django.urls import path

urlpatterns = [
    path('list/', views.todoView , name = 'todo'),
    path('add/', views.addTodo, name = 'addTodo'), 
    path('delete/<int:todo_id>/', views.deleteTodo, name = 'deleteTodo')
]