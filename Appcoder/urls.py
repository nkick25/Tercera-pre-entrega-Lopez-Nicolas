from django.urls import path
from django.contrib import admin
from Appcoder import views

urlpatterns = [
    ##path('admin/', admin.site.urls),
    ##path('Appcoder/', include('Appcoder.urls'))
    path('inicio/', views.inicio, name="inicio"),
    path('cursos/', views.curso, name="cursos"),
    path('estudiantes/', views.estudiante, name="estudiantes"),
    path('profesores/', views.profesor, name="profesores"),
    path('entregables/', views.entregable, name="entregables"),
    path('curso_formulario/', views.curso_form, name="curso_formulario"),
    path('estudiante_formulario/', views.estudiante_form, name="estudiante_formulario"),
    path('profesor_formulario/', views.profesor_form, name="profesor_formulario"),
    path('entregable_formulario/', views.entregables_form, name="entregable_formulario"),
    path('busqueda_camada/',  views.busqueda_camada, name="busqueda_camada"),
    path('resultados_camada/', views.resultados,name="resultados_camada"),
]