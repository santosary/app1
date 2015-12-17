# -*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from models import Categria, Un_medida, Produto, Endereco, Fornecedor, Orcamento
from django.core.exceptions import PermissionDenied
from django.forms import CheckboxSelectMultiple

class CategoriaAdmin(admin.ModelAdmin):
	list_disply = ('descricao')
	list_filter = ['descricao']
	search_fields = ['descricao']
	#formField = {models.ManyToManyField:{'widget':CheckboxSelectMultiple},}
	#fieldsets = [('Questões', {'fields': ['questao']}), ('Publicação', {'fields': ['publicacao']})]
	'''actions =['set_salario_zero', 'set_salario_mil', 'set_sobrenome'] #métodos definidos abaixo

	def set_salario_zero(self, request, queryset):#queryset contém os usuários selecionados na caixa de seleção
		if not request.user.is_superuser: #caso não seja super usuário levanta uma excessão 
			raise PermissionDenied
		else:
			for cliente in queryset: #loop nos usuários selcionados			
				cliente.salario = 0
				cliente.save()
	set_salario_zero.short_description = 'zera o salário do cidadão'''

admin.site.register(Categria, CategoriaAdmin)

class Un_medidaAdmin(admin.ModelAdmin):
	list_disply = ('descricao')
	list_filter = ['descricao']
	search_fields = ['descricao']

admin.site.register(Un_medida,Un_medidaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
	list_disply = ('descricao', 'categoria')
	list_filter = ['descricao', 'categoria']
	search_fields = ['descricao', 'categoria']

admin.site.register(Produto, ProdutoAdmin)

class EnderecoAdmin(admin.ModelAdmin):
	list_disply = ('rua', 'numero', 'bairro', 'cidade', 'cep', 'uf')
	list_filter = ['rua', 'bairro', 'cidade', 'uf']
	search_fields = ['rua', 'bairro', 'cidade', 'uf']

admin.site.register(Endereco, EnderecoAdmin)

class FornecedorAdmin(admin.ModelAdmin):
	list_disply = ('nome_fantasia', 'razao_social', 'cnpj', 'contato', 'email', 'fixo', 'tim', 'vivo', 'claro', 'oi', 'referencia')
	list_filter = ['nome_fantasia', 'razao_social', 'cnpj']
	search_fields = ['nome_fantasia', 'razao_social', 'cnpj']

admin.site.register(Fornecedor, FornecedorAdmin)

class OrcamentoAdmin(admin.ModelAdmin):
	list_disply = ('produto', 'fornecedor', 'data', 'preco_vista', 'preco_prazo', 'qt_parcelas')
	list_filter = ['produto', 'fornecedor']
	search_fields = ['produto', 'fornecedor']
	date_hierarchy = 'data'

admin.site.register(Orcamento, OrcamentoAdmin)