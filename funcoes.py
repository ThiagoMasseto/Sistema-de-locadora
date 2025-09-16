from classes import *
import time
import os

locadorasenai = Locadora()

def cadastrar_clientes():
    try:
        idcliente  = len(locadorasenai.getClientes()) + 1
        nome=(input("Nome--> "))

        cpf=int(input("CPF-->"))

        locadorasenai.cadastrarCliente(nome=nome,cpf=cpf, idcliente=idcliente)
        print("Cliente Adicionado com Sucesso!")

        time.sleep(1)
        os.system("cls")
    except Exception as e:
        print(f" Ocorreu um erro inesperado : {e}")
        os.system("pause")

def listar_clientes():
    os.system("cls")
    for itens in locadorasenai.getClientes():
        print(f"ID -> {itens.getId()}\nCLIENTE ->{itens.getNome()}\nCPF ->{itens.getCPF()}")
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
                    os.system("pause")
                    os.system("cls")
                case 2:
                    codigoitem=int(input("Código: "))
                    tituloitem=input("Titulo: ")
                    locadorasenai.cadastrarItem(codigo=codigoitem, titulo=tituloitem)
                    print("Item cadastrado com sucesso!")
                    os.system("pause")
                    os.system("cls")
                case 0:
                    os.system("cls")
                    break
                case _:
                    print("Opção Invalida!")
                    os.system("cls")
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

def controlar_emprestimos():
    while True:
        os.system("cls")
        print("=== Controle de Empréstimos ===")
        print("1 - Locar Item")
        print("2 - Devolver Item")
        print("0 - Voltar")
        escolha = int(input("--> "))

        if escolha == 0:
            break

        # Escolher cliente
        print("\nClientes:")
        for cliente in locadorasenai.getClientes():
            print(f"{cliente.getId()} - {cliente.getNome()}")
        id_cliente = int(input("Digite o ID do cliente: "))
        cliente = next((c for c in locadorasenai.getClientes() if c.getId() == id_cliente), None)

        if not cliente:
            print("Cliente não encontrado!")
            os.system("pause")
            continue

        if escolha == 1:  # Locar
            print("\nItens disponíveis:")
            for item in locadorasenai.getItens():
                if item.getDisponivel():
                    print(f"Código: {item.getCodigo()} | Título: {item.getTitulo()}")

            codigo_item = int(input("Digite o código do item: "))
            item = next((i for i in locadorasenai.getItens() if i.getCodigo() == codigo_item), None)

            if item and cliente.locar(item):
                print(f"Item '{item.getTitulo()}' alugado com sucesso!")
            else:
                print("Não foi possível locar (talvez já esteja alugado).")

        elif escolha == 2:  # Devolver
            print("\nItens locados pelo cliente:")
            for item in cliente.getItensLocados():
                print(f"Código: {item.getCodigo()} | Título: {item.getTitulo()}")

            codigo_item = int(input("Digite o código do item para devolver: "))
            item = next((i for i in cliente.getItensLocados() if i.getCodigo() == codigo_item), None)

            if item and cliente.devolver(item):
                print(f"Item '{item.getTitulo()}' devolvido com sucesso!")
            else:
                print("Esse item não está locado por este cliente.")

        os.system("pause")


