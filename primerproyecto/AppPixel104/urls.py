from django.urls import path
from AppPixel104.views import *
from django.contrib.auth.views import LogoutView


# urlpatterns = [
#     path("inicio/", inicio),
#     path("estudiantes/", estudiantes),
#     path("profesores/", profesores),
#     path("cursos/", cursos),
#     path("entregables/", entregables)
# ]

urlpatterns = [
    path("inicio/", inicio, name="coder-inicio"),
    path("estudiantes/", estudiantes, name="coder-estudiantes"),
    path("estudiantes/crear/", creacion_estudiante, name="coder-estudiantes-crear"),
    path("estudiantes/buscar/", buscar_alumnos, name="coder-estudiantes-buscar"),
    path("profesores/", profesores, name="coder-profesores"),
    path("profesores/crear/", creacion_profesores, name="coder-profesores-crear"),
    path("cursos/", cursos, name="coder-cursos"),
    path("cursos/borrar/<id>/", eliminar_curso, name="coder-cursos-borrar"),
    path("cursos/actualizar/<id>/", editar_curso, name="coder-cursos-editar"),
    
    path("entregables/", EntregablesList.as_view(), name="coder-entregables"),
    path("entregables/detalle/<pk>/", EntregableDetails.as_view(), name="coder-entregables-detalle"),
    path("entregables/crear/", EntregablesCreate.as_view(), name="coder-entregables-crear"),
    path("entregables/actualizar/<pk>/", EntregablesUpdate.as_view(), name="coder-entregables-actualizar"),
    path("entregables/<pk>/", EntregableDelete.as_view(), name="coder-entregables-borrar"),
    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("login/", iniciar_sesion, name="auth-login"),
    path("register/", registrar_usuario, name="user-register"),
    path("logout/", LogoutView.as_view(template_name="AppPixel104/logout.html"), name="auth-logout")

]
