from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject, EditTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'GET':
        return render(request, 'Login/login.html', {'form': UserCreationForm()})

    else:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if passwaord1 != password2:
            return HttpResponse("Las contraseñas no coinciden")

        try:
            user = User.objects.create_user(
                username=request.POST.get('username'),
                password=password1
            )
            user.save()
            #return HttpResponse("Usuario creado exitosamente")
            return redirect('home')
        except:
            return HttpResponse("El usuario ya existe")

def index(request):
    contexto = {"titulo": "Pagina de Inicio"}
    return render(request, "index/index.html", contexto)

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return render(request, 'about/about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects/projects.html', {'projects': projects})

def tasks(request):
    tasks = list(Task.objects.all())
    return render(request, 'Task/task.html', {'tasks': tasks})

def create_task(request, project_id=None):
    project = None
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    if request.method == "POST":
        form = CreateNewTask(request.POST)
        if project:
            form.fields.pop('project')  # Oculta el campo también en POST
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            if project:
                Task.objects.create(title=title, description=description, project=project)
                return redirect('projects_detail', id=project.id)
            else:
                selected_project = form.cleaned_data['project']
                Task.objects.create(title=title, description=description, project=selected_project)
                return redirect('tasks')
    else:
        form = CreateNewTask()
        if project:
            form.fields.pop('project')  # Oculta el campo en GET

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
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('tasks')

def task_edit(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = EditTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
            form = EditTask(instance=task)

    return render(request, 'Task/edit_task.html', {'form':form, 'task':task})