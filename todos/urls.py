from django.urls import path
from todos.views import (
    todo_list_list,
    todo_list_detail,
    create_todo_list,
    update_todo_list,
    delete_todo_list,
)


urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", create_todo_list, name="create_todo_list"),
    path("<int:id>/edit/", update_todo_list, name="update_todo_list"),
    path("<int:id>/delete/", delete_todo_list, name="delete_todo_list"),
]
