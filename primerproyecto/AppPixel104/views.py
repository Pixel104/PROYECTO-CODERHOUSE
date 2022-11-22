from django.http import HttpResponse
from AppPixel104.models import Curso, Estudiante, Profesor, Entregable
from AppPixel104.forms import ProfesorFormulario, EstudianteFormulario, CursoFormulario, UserRegisterForm
from django.shortcuts import render, redirect

#class based-views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # para crear usuario
from django.contrib.auth import authenticate, login #loguear usuario
from django.contrib.auth.mixins import LoginRequiredMixin #muestra algunas vistas solo si estas logueado
from django.contrib.auth.decorators import login_required #pprotege funciones solo para autenticados

# Create your views here.
def inicio(request):
    return render(request, "AppPixel104/index.html")

@login_required
def cursos(request):

    errores = ""

    #Validamos tipo de informacion
    if request.method =="POST":
        formulario = CursoFormulario(request.POST)

        #Cargamos informacion en el formulario
        if formulario.is_valid():
            #Recuperamos los datos
            data = formulario.cleaned_data
            #Creamos el curso
            curso = Curso(nombre=data["nombre"], camada=data["camada"])
            #guardamos en la DB
            curso.save()
        else:
            #Si el formulario no es valido, guardamos los errrores para mostrarlos
            errores = formulario.errors

    #Recuperamos cursos de la DB
    cursos = Curso.objects.all() #se obtienen todos los datos de ese modelo
    
    #Creamos Formulario vacio
    formulario = CursoFormulario()
    
    #Creamos el contexto
    contexto = {"listado_cursos": cursos, "formulario": formulario, "errores": errores}

    #retornamos la respuesta
    return render(request, "AppPixel104/cursos.html", contexto)




   # return render(request, "AppPixel104/cursos.html")

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect("coder-cursos")

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            curso.nombre=data["nombre"]
            curso.camada=data["camada"]
            curso.save()
            return redirect("coder-cursos")
        else:
            return render(request, "AppPixel104/editar_curso.html", {"formulario": formulario, "errores": formulario.errors})
    else:
        formulario = CursoFormulario(initial={"nombre": curso.nombre, "camada": curso.camada})
        return render(request, "AppPixel104/editar_curso.html", {"formulario": formulario, "errores": ""})


    
def estudiantes(request):
    return render(request, "AppPixel104/estudiantes.html")


def creacion_estudiante(request):

    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        #Validamos que el formulario no tenga problemas

        if formulario.is_valid():
            #Accedemos al formulacio que contiene
            #la informacion del formulario
            data = formulario.cleaned_data

            estudiantes = Estudiante(nombre=data["nombre"], apellido=data["apellido"], email=data["email"])
            estudiantes.save()

    formulario = EstudianteFormulario()
    return render(request, "AppPixel104/estudiantes_formulario.html", {"formulario": formulario})
    


def profesores(request):
    return render(request, "AppPixel104/profesores.html")


def creacion_profesores(request):
    

    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        #Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleanes_data
            data = formulario.cleaned_data

            profesor = Profesor(name=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])

            profesor.save()
    
    formulario = ProfesorFormulario()
    
    return render(request, "AppPixel104/profesores_formulario.html", {"formulario": formulario})



#def entregables(request):
    return render(request, "AppPixel104/entregables.html")


def buscar_curso(request):
    cursos = Curso.objects.all() #obtener todos los registros de este modelo

    contexto = {"listado_cursos": cursos}

    return render(request, "AppPixel104/cursos.html", contexto) 




def buscar_alumnos(request):

    if request.GET:
        nombre_alumno = request.GET.get("nombre_alumno", "")
        if nombre_alumno == "":
            estudiantes = []
        else:
            estudiantes = Estudiante.objects.filter(nombre__icontains=request.GET.get("nombre_alumno"))
        return render(request, "AppPixel104/busqueda_estudiantes.html", {"listado_alumnos": estudiantes} )
            
    return render(request, "AppPixel104/busqueda_estudiantes.html", {"listado_alumnos": []})


def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect("coder-cursos")


class EntregablesList(LoginRequiredMixin, ListView):
    model = Entregable
    template_name = "AppPixel104/detail_entregable.html"

class EntregableDetails(DetailView):
    model = Entregable
    template_name = "AppPixel104/detail_entregable.html"

class EntregablesCreate(CreateView):
    model = Entregable
    success_url = "coder/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    template_name = "AppPixel104/entregable_form.html"

class EntregablesUpdate(UpdateView):
    model = Entregable
    succes_url = "coder/entregables/"
    fields = ["fecha_de_entrega", "entregado"]
    
class EntregableDelete(DeleteView):
    model = Entregable
    suscces_url = "coder/entregables/"

def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("coder-inicio")
            else:
                return render(request, "AppPixel104/login.html", {"form": formulario, "errors": "Credenciales invalidas"})

        else:
            return render(request, "AppPixel104/login.html", {"form": formulario, "errors": formulario.errors})
    
    formulario = AuthenticationForm()
    return render(request, "AppPixel104/login.html", {"form": formulario, "errors": errors})

def registrar_usuario(request):

    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("coder-inicio")
        else:
            return render(request, "AppPixel104/register.html", { "form": formulario, "errors": formulario.errors})

    formulario  = UserRegisterForm()
    return render(request, "AppPixel104/register.html", { "form": formulario})
