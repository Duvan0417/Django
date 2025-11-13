from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

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

def create_task(request, project_id=None):
    project = None
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = CreateNewTask(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            # ✅ Asigna el proyecto directo si viene en la URL
            if project:
                Task.objects.create(title=title, description=description, project=project)
                return redirect('project_detail', id=project.id)
            else:
                selected_project = form.cleaned_data['project']
                Task.objects.create(title=title, description=description, project=selected_project)
                return redirect('tasks')
    else:
        # ✅ Si ya hay un proyecto, no mostramos el campo project
        form = CreateNewTask()
        if project:
            form.fields.pop('project')  # elimina el campo del formulario

    return render(request, 'Task/create_task.html', {'form': form, 'project': project})


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

def project_detail(request, id):
    print(id)
    project =  get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project=project)
    print(project)
    print(tasks)
    return render(request, 'projects/project_detail.html', {'project' : project,
    'tasks' : tasks})