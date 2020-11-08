"""frameworks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', views.alunosview, name='alunos'),
    path('alunos/<int:pk>', views.alunoshowview, name='alunos-show'),
    path('alunos/update/<int:pk>', views.alunoupdateview, name='alunos-update'),
    path('alunos/create', views.alunocreateview, name='alunos-create'),
    path('alunos/delete/<int:pk>', views.alunodeleteview, name='alunos-delete'),
    path('cursos/', views.cursosview, name='cursos'),
    path('cursos/<int:pk>', views.cursoshowview, name='cursos-show'),
    path('cursos/update/<int:pk>', views.cursoupdateview, name='cursos-update'),
    path('cursas/create', views.cursocreateview, name='cursos-create'),
    path('cursos/delete/<int:pk>', views.cursodeleteview, name='cursos-delete'),
    path('disciplinas/', views.disciplinasview, name='disciplinas'),
]
