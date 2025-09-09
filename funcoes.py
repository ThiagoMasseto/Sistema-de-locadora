from classes import *
import time
import os
locadorasenai = Locadora()
def cadastrar_clientes():
    nome=input("Nome--> ")
    cpf=int(input("CPF-->"))
    locadorasenai.cadastrarCliente(nome=nome,cpf=cpf)
    print("Cliente Adicionado com Sucesso!")
    time.sleep(1)
    os.system("cls")