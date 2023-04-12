from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo, TodoItems
from .forms import TodoForm, TodoItemsForm, UserCreationForm
from .filter import TodoFilter

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def home(req):
    user = req.user
    filter = TodoFilter()
    todos = Todo.objects.filter(user=user)
    if req.method == "Get":
        result = TodoFilter(req.GET, queryset=todos)
        todos = result.qs
    context = {
        "todos": todos,
        "user": user,
        "filter": filter,
    }

    return render(req, 'home.html', context)


def detailed(request, id):
    todo = Todo.objects.get(id=id)
    items = todo.todoitems_set.all()

    context = {
        "todo": todo,
        "items": items
    }
    return render(request, 'detaild.html', context)


def createTodo(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }

    return render(request, 'create.html', context)


def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }

    return render(request, 'update.html', context)


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')


def createItemTodo(request):
    form = TodoItemsForm()

    if request.method == "POST":
        form = TodoItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }

    return render(request, 'create item.html', context)


# def detailed(request, id):
#     todo = TodoItemsForm.objects.get(id=id)

#     items = todo.todoitems_set.all()

#     context = {
#         "todo": todo,
#         "items": items
#     }
#     return render(request, 'detaild.html', context)


def createUser(req):
    form = UserCreationForm()
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('/')
    context = {
        "form": form
    }
    return render(req, "signUp.html", context)


def loginUser(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        # ---> to find this user from database or not
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            return redirect('/')
    context = {
    }
    return render(req, "login.html", context)


def logoutUser(req):
    logout(req)
    return redirect('/')
