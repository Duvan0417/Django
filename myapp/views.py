from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    contexto = {"titulo":"Pagina de Inicio"}
    return render(request, "index/index.html", contexto)
def hello(request, id):
    print(type(id))
    return HttpResponse("<h1>Hello %s</h1>" % id)

def about(request):
    return HttpResponse("<h1>about</h1>")
