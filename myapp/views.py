from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Task
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
    return JsonResponse(projects, safe=False)

def tasks(request):
    #task = get_object_or_404(Task, title=title)
    return render(request, 'Task/task.html')
