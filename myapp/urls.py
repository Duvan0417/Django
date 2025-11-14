from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/detail/<int:id>', views.project_detail, name='projects_detail'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/<int:project_id>/', views.create_task, name='create_task'),
    path('projects/create/', views.create_project, name='create_project'),
    path('Hello/<str:username>', views.hello, name='hello'),
    path('login/', views.signup, name='login'),
    path('signup/', views.index, name='signup'),
]