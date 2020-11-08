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


def cursosview(request):
    queryset = Curso.objects.all()
    context = {'cursos': queryset}
    return render(request, 'cursos/list.html', context)


def disciplinasview(request):
    queryset = Disciplina.objects.all()
    context = {'disciplinas': queryset}
    return render(request, 'disciplinas/list.html', context)