from django .shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from todo import models
from todo .models import TodoItem
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        newUser=User.objects.create_user(username=username, email=email, password=password)
        newUser.save()
        return redirect("login")
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("todo_list")  # Redirect to a todo list view after login
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

def todo_list(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.method == "POST":
        title = request.POST.get("title")
        new_todo = TodoItem(title=title, user=request.user)
        new_todo.save()
    
    todos = TodoItem.objects.filter(user=request.user).order_by('-date')
    return render(request, "todo.html", {"todos": todos})


def delete_todo(request,srno):
    
    obj=models.TodoItem.objects.get(srno=srno)
    obj.delete()
    return redirect('/todo_list')

@login_required(login_url='/login')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = models.TodoItem.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('/todo_list')

    obj = models.TodoItem.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})

def signout(request):
    logout(request)
    return redirect('/login')