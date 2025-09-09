import os
import time
from funcoes import *
while True:
    try:
        os.system("cls")
        print("-- Sistema de Locadora --")
        print("Seja bem vindo!")
        print("1 - Cadastrar Clientes")
        print("2 - Listar Clientes")
        print("3 - Registrar itens para locação (filmes e jogos)")
        print("4 - Listar itens")
        print("5 - Controlar Emprestimos")
        print("0 - Sair")
        escolha=int(input("-->"))
        match escolha:
            case 1:
                cadastrar_clientes()
            case 2:
                listar_clientes()
            case 3:
                registrar_itens()
            case 4:
                listar_itens()
            case 5:
                controlar_emprestimos()
            case 0:
                print("Saindo...")
                time.sleep(1)
                os.system("cls")
                break
            case _:
                print("Opçao invalida, tente novamente.")
                os.system("pause")

    except Exception as e:
        print(f"Ocorreu um erro inesperado {e}")
        os.system("pause")
        os.system("cls")