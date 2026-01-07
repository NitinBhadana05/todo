
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.signup),
    path("login/",views.login,name="login"),
    path("todo_list/",views.todo_list,name="todo_list"),
     path('signout/', views.signout, name='signout'),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
]

