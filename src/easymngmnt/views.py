from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
	title = 'Bem vindo ao Easy Managment 1.5!'
	context = {
		"title": title,
	}
	return render(request, "home.html",context)


def lista_itens(request):
	title = 'Lista de Itens'
	queryset = Estoque.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "lista_itens.html",context)

def add_itens(request):
	form = CriaEstoque(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, 'Salvo com sucesso!')
		return redirect('/lista_itens')
	context = {
		"form": form,
		"title": "Adicionar Item",
	}
	return render(request, "add_itens.html", context)

def update_itens(request, pk):
	queryset = Estoque.objects.get(id=pk)
	form = EstoqueUpdate(instance=queryset)
	if request.method == 'POST':
		form = EstoqueUpdate(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Salvo com sucesso!')
			return redirect('/lista_itens')

	context = {
		'form':form
	}
	return render(request, 'add_itens.html', context)

def delete_itens(request, pk):
	queryset = Estoque.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Deletado com sucesso!')
		return redirect('/lista_itens')
	return render(request, 'delete_itens.html')

def detalhes(request, pk):
	queryset = Estoque.objects.get(id=pk)
	context = {
		"queryset": queryset,
	}
	return render(request, "detalhes.html", context)


def entrega(request, pk):
	queryset = Estoque.objects.get(id=pk)
	form = Entrega(request.POST or None, instance=queryset)
	if form.is_valid():
		itens = form.save(commit=False)
		itens.estoque_atual -= itens.entrega
		messages.success(request, "Entregue!" + ' ' + str(itens.estoque_atual)+ " " + str(itens.nome)+"(s)" + " restante(s) em Estoque")
		itens.save()

		return redirect('/lista_itens/')
	

	context = {
		"title": 'Remover ' + str(queryset.nome),
		"queryset": queryset,
		"form": form,
		"username": 'Removido por: ' + str(request.user),
	}
	return render(request, "add_itens.html", context)



def recebi(request, pk):
	queryset = Estoque.objects.get(id=pk)
	form = Recebi(request.POST or None, instance=queryset)
	if form.is_valid():
		itens = form.save(commit=False)
		itens.estoque_atual += itens.recebi
		itens.save()
		messages.success(request, "Recebido! " + str(itens.estoque_atual) + " " + str(itens.nome) + "(s)" + " restante(s) em Estoque")

		return redirect('/lista_itens/')
		
	context = {
			"title": 'Recebido ' + str(queryset.nome),
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_itens.html", context)


def aviso(request, pk):
	queryset = Estoque.objects.get(id=pk)
	form = Aviso(request.POST or None, instance=queryset)
	if form.is_valid():
		itens = form.save(commit=False)
		itens.save()
		messages.success(request, "Estoque mínimo de " + str(itens.nome) + " alterado para:	 " + str(itens.aviso))

		return redirect("/lista_itens")
	context = {
			"instance": queryset,
			"form": form,
		}
	return render(request, "add_itens.html", context)
