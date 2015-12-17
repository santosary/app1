# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categria, Un_medida, Fornecedor,Endereco, Produto, Orcamento
from .forms import ProdutoForm, CategoriaForm, Un_medidaForm, EnderecoForm, FornecedorForm
from django.contrib.auth.decorators import login_required

#https://www.youtube.com/watch?v=c0B1wdXT8Vc
#@login_required(login_url='/accounts/login/')
@login_required	
def home(request, template_name='compras/home.html'):
	produtos = Produto.objects.all()
	return render(request, template_name, {'f': produtos})

@login_required
def listarProduto (request, template_name='compras/listarProduto.html'):
	produtos = Produto.objects.all().order_by('descricao')
	return render(request, template_name, {'lista': produtos})

@login_required
def listarCategoria(request, template_name='compras/listarCategoria.html'):
	categoria = Categria.objects.all().order_by('descricao')
	return render(request, template_name, {'lista': categoria})

@login_required
def listarMedida(request, template_name='compras/listarMedida.html'):
	medida = Un_medida.objects.all().order_by('descricao')
	return render(request, template_name, {'lista': medida})

@login_required
def listarEndereco(request, template_name='compras/listarEndereco.html'):
	endereco = Endereco.objects.all()
	return render(request, template_name, {'lista': endereco})

@login_required
def listarFornecedor(request, template_name='compras/listarFornecedor.html'):
	fornecedor = Fornecedor.objects.all().order_by('nome_fantasia')
	return render(request, template_name, {'lista': fornecedor})

@login_required
def editarProduto(request, pk, template_name='compras/editar.html'):
	obj = get_object_or_404(Produto, pk=pk)
	form = ProdutoForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('listarProduto')
	return render(request, template_name, {'form': form})

@login_required
def editarCategoria(request, pk, template_name='compras/editar.html'):
	obj = get_object_or_404(Categria, pk=pk)
	form = CategoriaForm(request.POST or None, instance=obj)
	if form.is_valid():
		#us = form.save(commit=False)
		#us.usuario = request.user
		form.save()
		return redirect('listarCategoria')
	return render(request, template_name,{'form': form})

@login_required
def editarMedida(request, pk, template_name='compras/editar.html'):
	obj = get_object_or_404(Un_medida, pk=pk)
	form = Un_medidaForm(request.POST or None, instance=obj)
	if form.is_valid():  
		form.save()
		return redirect('listarMedida')
	return render(request, template_name, {'form': form})

@login_required
def editarEndereco(request, pk, template_name='compras/editar.html'):
	obj = get_object_or_404(Endereco, pk=pk)
	form = EnderecoForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('listarEndereco')
	return render(request, template_name, {'form': form})

@login_required
def editarFornecedor(request, pk, template_name='compras/editar.html'):
	obj = get_object_or_404(Fornecedor, pk=pk)
	#end = Endereco.objects.filter(id=obj.endereco.id)#retorna mais de um objeto
	end = Endereco.objects.filter(fornecedor=obj)
	print end	
	form = FornecedorForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
		return redirect('listarFornecedor')
	return render(request, template_name, {'form': form})

@login_required
def listarEnderecosFornecedor(request, pk, template_name='compras/listEnderecos.html'):
	obj = get_object_or_404(Fornecedor, pk=pk)
	end = Endereco.objects.filter(fornecedor=obj)
	return render(request, template_name, {'lista':end})

@login_required
def produtoBuscaFornecedores(request, pk, template_name='compras/listarFornecedor.html'):
	p = get_object_or_404(Produto, pk=pk)
	f = p.fornecedor.all().order_by('nome_fantasia')
	return render(request, template_name, {'lista':f})

@login_required
def fornecedorBuscaProduto(request,pk, template_name='compras/listarProduto.html'):
	f = get_object_or_404(Fornecedor, pk=pk)
	p = f.produto_set.all().order_by('-categoria', 'descricao')
	return render(request, template_name, {'lista':p})

@login_required
def produtoPorCategoria(request, pk, template_name='compras/listarProduto.html'):
	p = get_object_or_404(Produto, pk=pk)
	c = p.categoria
	res = Produto.objects.filter(categoria=c)
	return render(request, template_name, {'lista':res})

@login_required
def cotacao(request, pk, template_name='compras/listarCotacao.html'):
	cot = get_object_or_404(Produto, pk=pk)
	lis = Orcamento.objects.filter(produto=cot).order_by('-data')
	return render(request, template_name, {'lista':lis})

# variavel = get_object_or_404(Produto, pk=request.POST.get('categoria'))
'''e = Entry.objects.get(id=3)
e.authors.all() # Retorna todos os objetos Author desta Entry.
e.authors.count()
e.authors.filter(name__contains='John')

a = Author.objects.get(id=5)
a.entry_set.all() # Retorna todos os objetos Entry desse Author.


>>> b = Blog.objects.get(id=1)
>>> b.entry_set.all() # Retorna todas os objetos Entry relacionados ao Blog.
https://django-portuguese.readthedocs.org/en/1.0/topics/db/queries.html'''

def teste(request, template_name='compras/teste.html'):
	fornecedor = Fornecedor.objects.all()
	return render(request, template_name, {'lista':fornecedor})