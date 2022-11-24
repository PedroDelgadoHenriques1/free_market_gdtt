from classes import *

def busca_empresa_rec(self, chave):
	if type(self) == Empresa:
		if self.id == None: return 0
		if self.id == chave: return 1
		else:
			if self.id > chave and esquerda_id != None:
				busca_empresa_rec(esquerda_id, chave)
			else self.id < chave and self.direita_id != None:
				busca_empresa_rec(self.direita_id, chave)

