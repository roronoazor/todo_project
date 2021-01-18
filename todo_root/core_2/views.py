from django.shortcuts import render, get_object_or_404, redirect
from core_2.models import Todo
from django.urls import reverse

# Create your views here.
def list_todos(request, *args, **kwargs):

    todos = Todo.objects.all()
    context = dict()
    context["todos"] = todos
    return render(request, "core_2/index.html", context)


def todo_detail(request, *args, **kwargs):

    todo = get_object_or_404(Todo, pk=kwargs['id'])
    context = dict()
    context["todo"] = todo
    return render(request, "core_2/details.html", context)


def todo_delete(request, *args, **kwargs):
    
    todo = get_object_or_404(Todo, pk=kwargs['id'])
    todo.delete()
    return redirect(reverse("list_todos"))