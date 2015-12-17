# -*- coding: utf-8 -*-

from django.db import models

class Categria(models.Model):
	descricao = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.descricao

class Un_medida(models.Model):
	descricao = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.descricao

class Fornecedor(models.Model):
	nome_fantasia = models.CharField(max_length=80, unique=True)
	razao_social = models.CharField(max_length=80, unique=True)
	cnpj = models.CharField(max_length=18, default='00.000.000/0001-97', unique=True)
	#cpf = models.CharField(max_length=14, default= '000.000.000-00', blank=True)

	def __unicode__(self):
		return '%s %s %s %s' %(self.nome_fantasia,self.razao_social,self.cnpj)

class Produto(models.Model):
	descricao = models.CharField(max_length=50, unique=True)
	categoria = models.ForeignKey(Categria)
	un_medida = models.ManyToManyField(Un_medida)
	fornecedor = models.ManyToManyField(Fornecedor)

	def __unicode__(self):
		return self.descricao+' '+unicode(self.categoria)

class Endereco(models.Model):
	rua = models.CharField(max_length=50)
	numero = models.CharField(max_length=10)
	bairro = models.CharField(max_length=40)
	cidade = models.CharField(max_length=50)
	cep = models.CharField(max_length=10)
	uf = models.CharField(max_length=2)
	contato = models.CharField(max_length=80)
	email = models.EmailField(max_length=75)
	fixo = models.CharField(max_length=13, default='(38)3000-0000')
	tim = models.CharField(max_length=14, default='(38)0000-0000')
	vivo = models.CharField(max_length=24, default='(38)0000-0000')
	claro = models.CharField(max_length=14, default='(38)0000-0000')
	oi = models.CharField(max_length=14, default='(38)0000-0000')
	referencia = models.CharField(max_length=100)
	fornecedor = models.ForeignKey(Fornecedor)

	def __unicode__(self):
		return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %(self.rua, self.numero, self.bairro, self.cidade, self.cep, self.uf, self.contato,unicode(self.email),self.fixo,self.tim,self.vivo,self.claro,self.oi,self.referencia, self.fornecedor)

class Orcamento(models.Model):
	produto = models.ForeignKey(Produto)
	fornecedor = models.ForeignKey(Fornecedor)
	data = models.DateField()
	medida = models.ForeignKey(Un_medida)
	preco_vista = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
	preco_prazo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
	qt_parcelas = models.IntegerField(default=1)
	preco_atacado = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	quantidade = models.CharField(max_length=16, blank=True)

	def __unicode__(self):
		return '%s %s %s %s %s %s' %(unicode(self.produto), unicode(self.fornecedor), unicode(self.data),unicode(self.preco_vista),
				unicode(self.preco_prazo), unicode(self.qt_parcelas))