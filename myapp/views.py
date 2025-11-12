from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
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

    if request.method == "POST":
        form = CreateNewTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            projects = Project.objects.all()
            Task.objects.create(title=title, description=description, project=projects[0])
            #return render(request, 'Task/create_task.html', {'form': CreateNewTask(), 'success': True})
            return redirect('tasks')
    else:
        form = CreateNewTask()
    return render(request, 'Task/create_task.html', {'form': form})

def create_project(request):
    if request.method == "POST":
        form = CreateNewProject(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Project.objects.create(name=name)
            return redirect('projects')
    else:
        form = CreateNewProject()
    return render(request, 'projects/create_project.html', {'form': form})