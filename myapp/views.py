from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Task
from .forms import CreateNewTask
# Create your views here.
def index(request):
    contexto = {"titulo":"Pagina de Inicio"}
    return render(request, "index/index.html", contexto)
def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return render(request, 'about/about.html')

def projects(request):
    projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):
    tasks = list(Task.objects.all())
    return render(request, 'Task/task.html', {'tasks' : tasks})

def create_task(request):
    form = CreateNewTask()
    return render(request, 'Task/create_task.html', {'form': form})