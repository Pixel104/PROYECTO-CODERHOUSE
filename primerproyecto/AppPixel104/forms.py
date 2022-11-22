from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(min_length=3, max_length=50)
    apellido = forms.CharField(min_length=3, max_length=50)
    email = forms.EmailField()    


class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electronico")
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "last_name", "password1", "password2"]
