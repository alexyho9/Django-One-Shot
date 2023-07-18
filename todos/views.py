from django.shortcuts import render
from todos.models import TodoList


# Create your views here.
def todo_list_list(request):
    tasks = TodoList.objects.all()
    context = {
        "todo_list_list": tasks,
    }
    return render(request, "todos/list.html", context)
