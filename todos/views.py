from django.shortcuts import render, get_object_or_404
from todos.models import TodoList


# Create your views here.
def todo_list_list(request):
    task_list_list = TodoList.objects.all()
    context = {
        "todo_list_list": task_list_list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    task_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_detail": task_list,
    }
    return render(request, "todos/detail.html", context)
