from classes import *
import time
import os

locadorasenai = Locadora()

def cadastrar_clientes():
    try:
        nome=(input("Nome--> "))

        cpf=int(input("CPF-->"))

        locadorasenai.cadastrarCliente(nome=nome,cpf=cpf)
        print("Cliente Adicionado com Sucesso!")

        time.sleep(1)
        os.system("cls")
    except Exception as e:
        print(f" Ocorreu um erro inesperado : {e}")

def listar_clientes():
    os.system("cls")
    for itens in locadorasenai.getClientes():
        print(f"CLIENTE ->{itens.getNome()}\nCPF ->{itens.getCPF()}")
        print(20 * "-")
    os.system("pause")
    os.system("cls")

def registrar_filme():
    pass

def registar_jogo():
    pass
