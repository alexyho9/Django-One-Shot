from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


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


def todo_list_create(request):
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


def todo_list_update(request, id):
    tasks = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=tasks)

    context = {
        "todo_list_detail": tasks,
        "todo_form": form,
    }
    return render(request, "todos/update.html", context)


def todo_list_delete(request, id):
    tasks = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        tasks.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()

    context = {
        "item_form": form,
    }
    return render(request, "todos/item_create.html", context)


def todo_item_update(request, id):
    item = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm(instance=item)

    context = {
        "item_form": form,
    }
    return render(request, "todos/item_update.html", context)
