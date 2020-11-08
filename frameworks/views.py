from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *


class AlunosForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idcurso']


def alunosview(request):
    queryset = Aluno.objects.all()
    context = {'alunos': queryset}
    return render(request, 'alunos/list.html', context)


def alunocreateview(request):
    form = AlunosForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('alunos')
    queryset = Curso.objects.all()
    context = {'cursos': queryset, 'form': form}
    return render(request,'alunos/create.html', context)


def alunodeleteview(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
    return redirect('alunos')


def alunoupdateview(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    cursos = Curso.objects.all()
    context = {'aluno': aluno, 'cursos': cursos}
    if request.method == 'POST':
        form = AlunosForm(request.POST or None, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos')
    return render(request, 'alunos/update.html', context)


def alunoshowview(request, pk):
    queryset = get_object_or_404(Aluno, pk=pk)
    context = {'aluno': queryset}
    return render(request, 'alunos/show.html', context)



class CursosForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']


def cursosview(request):
    queryset = Curso.objects.all()
    context = {'cursos': queryset}
    return render(request, 'cursos/list.html', context)


def cursocreateview(request):
    form = CursosForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('cursos')
    queryset = Disciplina.objects.all()
    context = {'disciplinas': queryset, 'form': form}
    return render(request,'cursos/create.html', context)


def cursodeleteview(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
    return redirect('cursos')


def cursoupdateview(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    disciplinas = Disciplina.objects.all()
    context = {'curso': curso, 'disciplinas': disciplinas}
    if request.method == 'POST':
        form = CursosForm(request.POST or None, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    return render(request, 'cursos/update.html', context)


def cursoshowview(request, pk):
    queryset = get_object_or_404(Curso, pk=pk)
    context = {'curso': queryset}
    return render(request, 'cursos/show.html', context)


def disciplinasview(request):
    queryset = Disciplina.objects.all()
    context = {'disciplinas': queryset}
    return render(request, 'disciplinas/list.html', context)