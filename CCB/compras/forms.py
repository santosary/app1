# -*- coding: utf-8 -*-

from django import forms

from models import Categria, Un_medida, Produto, Endereco, Fornecedor, Orcamento

#class JobForm(models.ModelForm): #fields class Meta: model = Job fields = "__all__" 

class CategoriaForm(forms.ModelForm):
	class Meta:
		model = Categria
		fields = "__all__"

	def clean_categoria(self):
		descricao = self.cleaned_data.get('descricao')
		if Categoria.objects.filter(descricao=descricao):
			raise forms.ValidetionError('Esta categoria já está cadastrada')
		return descricao

class Un_medidaForm(forms.ModelForm):
	class Meta:
		model = Un_medida
		fields = "__all__"

class ProdutoForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = "__all__"


class EnderecoForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = "__all__"

class FornecedorForm(forms.ModelForm):
	class Meta:
		model = Fornecedor
		fields = "__all__"

class OrcamentoForm(forms.ModelForm):
	class Meta:
		model = Orcamento
		fields = "__all__"
#https://django-bootstrap-form.readthedocs.org/en/latest/     plugin