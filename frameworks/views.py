from django.shortcuts import render
from .models import *


def alunosview(request):
    queryset = Aluno.objects.all()
    context = {'alunos': queryset}
    return render(request, 'alunos/list.html', context)


def cursosview(request):
    queryset = Curso.objects.all()
    context = {'cursos': queryset}
    return render(request, 'cursos/list.html', context)


def disciplinasview(request):
    queryset = Disciplina.objects.all()
    context = {'disciplinas': queryset}
    return render(request, 'disciplinas/list.html', context)