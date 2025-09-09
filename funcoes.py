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
                    codigoitem=int(input("Código: "))
                    tituloitem=input("Titulo: ")
                    locadorasenai.cadastrarItem(codigo=codigoitem, titulo=tituloitem)
                    print("Item cadastrado com sucesso!")
                case 2:
                    codigoitem=int(input("Código: "))
                    tituloitem=input("Titulo: ")
                    locadorasenai.cadastrarItem(codigo=codigoitem, titulo=tituloitem)
                    print("Item cadastrado com sucesso!")
                case 0:
                    break
                case _:
                    print("Opção Invalida!")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            os.system("pause")

def listar_itens():
    os.system("cls")
    for itens in locadorasenai.getItens():
        print(f"Titulo ->{itens.getTitulo()}\nCódigo ->{itens.getCodigo()}")
        print(20 * "-")
    os.system("pause")
    os.system("cls")

