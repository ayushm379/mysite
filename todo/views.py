from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.utils import timezone

# Create your views here.
def todoView(request):
    all_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items':all_items})

def addTodo(request):
    data = request.POST['content']
    new_item = TodoItem(content = data, date = timezone.now())
    new_item.save()
    return HttpResponseRedirect('/todo/list')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id = todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/list')