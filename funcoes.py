from classes import *
locadorasenai = Locadora()
def cadastrar_clientes():
    nome=input("Nome--> ")
    cpf=int(input("CPF-->"))
    locadorasenai.cadastrarCliente(nome=nome,cpf=cpf)
    print("Cliente Adicionado com Sucesso!")