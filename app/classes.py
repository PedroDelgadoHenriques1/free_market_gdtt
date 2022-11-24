from datetime import datetime, timedelta

import itertools

iter_id = itertools.count()

# print("Hoje é ", datetime.today())

enterprises = []
devs = []
projects = []

class Empresa:

	ads = []
	
	iteration = iter_id

	def __init__(self, enterprise, cnpj, user, password, address):
		self.id = next(self.iteration)
		self.direita_id = self.id + 1
		self.esquerda_id = self.id - 1
		self.enterprise = enterprise
		self.cnpj = cnpj
		self.user = user
		self.password = password
		self.address = address
		self.data_criacao =  datetime.now()
		self.data_alteracao = datetime.now()
		self.anuncios = 0
		self.projetos = 0

	def __str__(self):
		return self.enterprise
	
	def add_anuncio(self, descricao, valor, prazo_final):
		Anuncio.__init__(Anuncio, self.id, descricao, valor, prazo_final)
		print("ID de anúncio: ", Anuncio.id, "\n Descrição: ", Anuncio.descricao,"\n valor: R$", Anuncio.valor, "\n Prazo final: ", Anuncio.prazo_final) 
		return Anuncio
		
	def enviar_mensagem():
		pass
		self.anuncios += 1
		print("Número de anúncios atual: ", self.anuncios)
		return self.anuncios

	def modify_address(self, new_address):
		self.address = new_address
		return
	def print_empresa(self):
		print(
			"ID: ", self.id, 
			"\n Razão Social: ", self.enterprise, 
			"\n CNPJ: ", self.cnpj, 
			"\núltima alteração: ",  self.data_alteracao
		)
		
	def add_enterprise(e):
		if isinstance(e, Empresa):
			enterprises.append(e)
		else:
			print("operação inválida")
	
class Desenvolvedor:
	iteration = iter_id

	def __init__(self, name, cpf, user, password):
	  	self.id = next(Desenvolvedor.iteration)
	  	self.name = name
	  	self.cpf = cpf
	  	self.user = user
	  	self.password = password
	  	self.level = 1
	  	self.insigneas = ["new member"]
	  	self.projetos = []
	  	self.skills = []
	  	self.data_criacao = datetime.now()
	  	self.data_alteracao = datetime.now()
	
	
	def __str__(self):
		return self.name	

	def level_up(self):
		return 
	def new_insignea():
		return
	
	def modify_address(self, new_address):
		self.address = new_address
		return
	
	def new_project(self,  Empresa, Anuncio):
		Projeto.__init__(Projeto, Anuncio) #(self, Anuncio)
		return
	def todos_anuncios():
		pass
	def visualizar_anuncio(Anuncio):
		pass
	def enviar_mensagem():
		pass 
	
	def get_projetos(self):
		return self.projects
	
	class Portfolio():
		def __init__(self, name, cpf, user, descricao, curriculum):
			self.descricao = descricao
			self.curriculum = curriculum		

class Anuncio:
	iteration = iter_id

	def __init__(self, Empresa, descricao, valor, prazo_final):
		self.id = next(Anuncio.iteration)
		self.Empresa = Empresa
		self.descricao = descricao
		self.valor = valor
		self.data_criacao =  datetime.now()
		self.data_alteracao = datetime.now()
		self.prazo = self.data_criacao + timedelta(days=60)
		prazo_final = timedelta(days = 60)
		self.prazo_final = datetime.today() + prazo_final
	
	def delete_anuncio ():
		delete

class Projeto(Anuncio):
	iteration = iter_id
	
	def __init__(self, Anuncio):
		self.id = next(Projeto.iteration)
		empresa_id = Anuncio.id
		self.valor = Anuncio.valor
		self.prazo = Anuncio.prazo_final
		self.status = "new"
		self.data_criacao =  datetime.now()
		self.data_alteracao = datetime.now()
		self.prox_entrega = self.data_criacao.day + 30
		
		#constructor classe pai
		Anuncio.__init__(Empresa, Anuncio.descricao, Anuncio.valor, Anuncio.prazo_final)
		
		
class Chat:

	def __init__(self, Empresa, Desenvolvedor, mensagens, data_envio, Anuncio):
		self.id = [Empresa.id, Desenvolvedor.id]
		self.empresa_id= empresa_id
		self.desenvolvedor_id = desenvolvedor_id
		self.mensagens = mensagens
		self.data_envio = data_envio
		self.Anuncio = Anuncio
		self.data_criacao =  datetime.now()
		self.data_alteracao = datetime.now()
		
	def new_message():
		return
		
	def close_chat():
		return



