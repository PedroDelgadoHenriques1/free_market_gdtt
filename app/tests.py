from classes import *

e1 = Empresa(
	"Prucho Mello Brechó LTDA",
	"43456935000190",
	"user@dominio.com",
	"password",
	"address, 123"
	)
e2 = Empresa(
	"Sampaio Barreto Lavanderia EPP",
	"43456935000190",
	"user@dominio.com",
	"password",
	"address, 123"
	)
e3 = Empresa(
	"Mattos Valente Floricultura LTDA",
	"43456935000190",
	"user@dominio.com",
	"password",
	"address, 123"
	)
a1 = Anuncio( #(self, Empresa, descricao, valor, prazo_final)
	e2,
	"IA para segurança no trabalho",
	1200.00,
	360
	)
d1 = Desenvolvedor(
	"Adrian Johnes",
	"01744919290",
	"user@hacker.com",
	"notthepassword123"
	)

"""
print("id empresa", e1, ": ", e1.id)
print("id empresa", e2, ": ", e2.id)

print("Anúncios da empresa", e2, "antes:", e2.anuncios) 

print("Anúncios da empresa", e2, "depois:", e2.anuncios) 
"""


devs = []
ads = []


e2.add_anuncio("Automação de preenchimento de nota fiscal", 700.00, 180)
p1 = Projeto(a1)
d1.projetos.append(p1)

#add enterprise, ad, project, dev, 
#all ads of enterprise X
#one ad of one enterprise

Empresa.add_enterprise(e1)


