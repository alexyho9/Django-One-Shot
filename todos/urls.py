from django.urls import path
from todos.views import (
    todo_list_list,
    todo_list_detail,
    todo_list_create,
    todo_list_update,
    todo_list_delete,
    todo_item_create,
    todo_item_update,
)


urlpatterns = [
    path("", todo_list_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", todo_list_create, name="create_todo_list"),
    path("<int:id>/edit/", todo_list_update, name="update_todo_list"),
    path("<int:id>/delete/", todo_list_delete, name="delete_todo_list"),
    path("items/create/", todo_item_create, name="create_todo_item"),
    path("items/<int:id>/edit/", todo_item_update, name="update_todo_item"),
]
