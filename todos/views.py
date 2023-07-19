from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList
from todos.forms import TodoListForm


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


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm()

    context = {
        "todo_form": form,
    }
    return render(request, "todos/create.html", context)
