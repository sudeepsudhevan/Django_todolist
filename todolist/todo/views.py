from django.shortcuts import render, redirect
from .models import Todo
from .form import todoForm


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    form = todoForm()
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todolist")
    return render(request, "todo_list.html", {"todos": todos, "form": form})


def todo_update(request, pk):
    todo = Todo.objects.get(id=pk)
    form = todoForm(instance=todo)
    if request.method == "POST":
        form = todoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todolist")

    return render(request, "todo_list.html", {"form": form})


def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("todolist")
    return render(request, "todo_delete.html", {"todo": todo})
