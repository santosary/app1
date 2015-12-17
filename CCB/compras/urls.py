# -*- coding:utf-8 -*-

from django.conf.urls import patterns, url, include

urlpatterns = patterns('compras.views',
	url(r'^$', 'home', name='home'),
	#url(r'^accounts/login/$', auth_views.login),
	url(r'^listarCategoria/$', 'listarCategoria', name='listarCategoria'),
	url(r'^listarProduto/$', 'listarProduto', name='listarProduto'),
	url(r'^listarMedida/$', 'listarMedida', name='listarMedida'),
	url(r"^listarEndereco/$", 'listarEndereco', name='listarEndereco'),
	url(r"^listarFornecedor/$", 'listarFornecedor', name='listarFornecedor'),
	

	#url(r"^teste/", 'teste', name='teste'),
	#url(r'^[A-Za-z]*/', 'listar', name='listar'),
	url(r'^produtoPorCategoria/(?P<pk>\d+)/', 'produtoPorCategoria', name='produtoPorCategoria'),
	url(r'^fornecedorBuscaProduto/(?P<pk>\d+)/', 'fornecedorBuscaProduto', name='fornecedorBuscaProduto'),
	url(r'^produtoBuscaFornecedores/(?P<pk>\d+)/', 'produtoBuscaFornecedores', name='produtoBuscaFornecedores'),
	url(r'^listEnderecos/(?P<pk>\d+)/', 'listarEnderecosFornecedor', name='listEndForn'),
	url(r'^editarProduto/(?P<pk>\d+)/', 'editarProduto', name='editarProduto'),
	url(r'^editarCategoria/(?P<pk>\d+)/', 'editarCategoria', name='editarCategoria'),
	url(r'^editarMedida/(?P<pk>\d+)/', 'editarMedida', name='editarMedida'),
	url(r'^editarEndereco/(?P<pk>\d+)/', 'editarEndereco', name='editarEndereco'),
	url(r'^editarFornecedor/(?P<pk>\d+)/', 'editarFornecedor', name='editarFornecedor'),
	url(r'^cotacao/(?P<pk>\d+)/', 'cotacao', name='cotacao'),
)