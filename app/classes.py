from datetime import datetime
import itertools

class Empresa:
	iter_id = itertools.count()

	def __init__(self, enterprise, cnpj, user, password, address):
		self.id = next(self.iter_id)
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

class Desenvolvedor:
	iter_id = itertools.count()

	def __init__(self, name, cpf, user, password, skills):
	  	self.id = next(Desenvolvedor.iter_id)
	  	self.name = name
	  	self.cpf = cpf
	  	self.user = user
	  	self.password = password
	  	self.skills = skills
	  	self.level = 1
	  	self.insigneas = "new member"
	  	self.projetos = 0

	def __str__(self):
		return self.name	

	def level_up(self):
		return 

class Portfolio(Desenvolvedor):
	def __init__(self, id, name, cpf, user, password, email, skills, level, insigneas, descricao, curriculum):
		self.descricao = descricao
		self.curriculum = curriculum
		
		#constructor classe pai
		Desenvolvedor.__init__(self) 

class Projeto:
	iter_id = itertools.count()

	def __init__(self, id, empresa_id, descricao, valor, prazo, data_criacao, data_alteracao):
		self.id = id
		self.empresa_id = empresa_id
		self.descricao = descricao
		self.valor = valor
		self.prazo = prazo
		self.data_criacao = data_criacao
		self.data_alteracao = data_alteracao
		

class Contrato(Projeto):
	def __init__(self, id, empresa_id, descricao, valor, prazo, data_criacao, data_alteracao, prox_entrega, status):
		self.prox_entrega = prox_entrega
		self.status = status
		
		#constructor classe pai
		Projeto.__init__(self)
		
class Chat:
	iter_id = itertools.count()

	def __init__(self, empresa_id, desenvolvedor_id, mensagens, data_envio, projeto):
		self.empresa_id= empresa_id
		self.desenvolvedor_id = desenvolvedor_id
		self.mensagens = mensagens
		self.data_envio = data_envio
		self.projeto = projeto

e1 = Empresa( 
		"Coca-Cola",
		"31643708000194", 
		"alvo@domail.com",
		'asdas221\#', #probably not the password
		"Rua do mel, 123"	
	)

d1 = Desenvolvedor(
		"john",
		84446724169,
		"dullboy@harvard.com",
		'asdas221\#', #probably not the password		 
  		["chess", "catan"]
	)

print(e1.enterprise + " is at " + e1.address)  	
print(d1.name + " could never " + d1.skills[0]) 



