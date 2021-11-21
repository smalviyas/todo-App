from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('todo/', views.todonow, name='currenttodo'),
    path('create/', views.createtodo, name='createtodo'),
    path('', views.home, name='home'),
    path('todo/<int:todo_pk>', views.detailtodo, name='detailtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('completedlist/', views.completedlist, name='completedlist'),

]
