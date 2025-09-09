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

def registrar_itens():
    while True:
        try:
            print("O que voce deseja registrar?\n1-Filme\n2-Jogo\n0-Sair")
            escolha=int(input("-->"))
            os.system("cls")
            match escolha:
                case 1:
                    pass
                case 2:
                    pass
                case 0:
                    break
                case _:
                    print("Opção Invalida!")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")

