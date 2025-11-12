from django import forms


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    description = forms.CharField(label="Description de la tarea", required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del projecto", max_length=200)