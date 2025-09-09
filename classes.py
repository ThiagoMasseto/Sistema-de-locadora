class Locadora:
    def __init__(self, clientes,itens):
        self.__Clientes = clientes
        self.__Itens = itens
        self.__listaclientes= []
        self.__listaitens=[]
    
    def cadastro_cliente(self, cliente):
        self.__listaclientes.append(cliente)

    def cadastro_item(self, item):
        self.__listaitens.append(item)
    
    def listar_cliente(self):
        return self.__listaclientes
    
    def listar_itens(self):
        return self.__listaitens
    

