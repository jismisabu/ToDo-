"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work.views import Registration,Signin,Add_task,Delete_Task,Task_edit,Signout,User_del,Update_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',Registration.as_view()),
    path('log/',Signin.as_view(),name="signin"),
    path('',Add_task.as_view(),name="index"),
    path('delete/<int:pk>',Delete_Task.as_view(),name="delete"),
    path('index/update/<int:pk>',Task_edit.as_view(),name="edit"),
    path('signout/',Signout.as_view(),name='logout'),
    path('del_user/<int:pk>',User_del.as_view(),name="del"),
    path('u_user/<int:pk>',Update_user.as_view(),name="update")

]
