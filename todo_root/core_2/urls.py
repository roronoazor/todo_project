from django.urls import path
from core_2.views import *

urlpatterns = [
    path("index/", list_todos, name="list_todos"),
    path("details/<int:id>/", todo_detail, name="get_todo"),
    path("details/<int:id>/delete", todo_delete, name="delete_todo"),

]

