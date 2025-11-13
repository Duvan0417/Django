from django import forms
from myapp.models import Project


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    description = forms.CharField(label="Description de la tarea", required=False)
    project = forms.ModelChoiceField(queryset=None)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 🔥 Aquí asignamos el queryset correctamente cuando se crea el formulario
        self.fields['project'].queryset = Project.objects.all()

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del projecto", max_length=200)