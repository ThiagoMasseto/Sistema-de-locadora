class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []

    #Metodo Gets e Sets
    def getClientes(self):
        return self.__clientes
    
    def getItens(self):
        return self.__itens
    
    def setClientes(self, clientes):
        self.__clientes = clientes
        return clientes
    
    def setItens(self, itens):
        self.__itens = itens
        return itens
    
    #---------------------------------------------------
    def cadastrarCliente(self,nome, cpf, idcliente):
        cliente = Cliente(nome=nome, cpf=cpf, idcliente=idcliente)
        self.__clientes.append(cliente)

    def cadastrarItem(self, codigo,titulo):
        item= Item(codigo=codigo, titulo=titulo)
        self.__itens.append(item)

    def listarCliente(self):
        return self.__clientes
    
    def listarItem(self):
        return self.__itens
#-----------------------------------------------
class Item:
    def __init__(self, codigo, titulo):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = True

    #---------------------------------------------
    #metodos Gets e Sets

    def getCodigo(self):
        return self.__codigo
    
    def getTitulo(self):
        return self.__titulo
    
    def getDisponivel(self):
        return self.__disponivel
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
        return codigo
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
        return titulo
    #-------------------------------------------
    
    def alugar(self,):
        self.__disponivel = False

    def devolver(self,):
        self.__disponivel = True
#-----------------------------------------------
class Filme(Item):
    def __init__(self, genero, duracao):
        self.__Genero = genero
        self.__Duracao = duracao

#------------------------------------------------
    #metodos gets e sets

    def getGenero(self):
        return self.__Genero
    
    def getDuracao(self):
        return self.__Duracao
    
    def setGenero(self, genero):
        self.__Genero = genero
        return genero
    
    def setDuracao(self, duracao):
        self.__Duracao = duracao
        return duracao
#-----------------------------------------------
class Jogo(Item):
    def __init__(self,plataforma, faixaetaria):
        self.__Plataforma = plataforma
        self.__Faixaetaria = faixaetaria
#-----------------------------------------------
    #metodos gets e sets

    def getPlataforma(self):
        return self.__Plataforma
    
    def getFaixaetaria(self):
        return self.__Faixaetaria
    
    def setPlataforma (self, plataforma):
        self.__Plataforma = plataforma

    def setFaixaetaria (self, faixaetaria):
        self.__Faixaetaria = faixaetaria
#-----------------------------------------------
class Cliente:
    def __init__(self, nome, cpf, idcliente):
        self.__nome = nome
        self.__cpf= cpf
        self.__id= idcliente
        self.__itensLocados= []

    #Metodos Gets e Sets
    def getNome(self):
        return self.__nome
    
    def getId(self):
        return self.__id
    
    def getCPF(self):
        return self.__cpf
    
    def getItensLocados(self):
        return self.__itensLocados
    #-------------------------------------
    def setNome(self, nome):
        self.__nome = nome
        return nome
    
    def setCpf(self, cpf):
        self.__cpf = cpf
        return cpf
    
    def setItensLocados(self, itensLocados):
        self.__itensLocados = itensLocados
        return itensLocados
    
    def locar(self, codigo, titulo, disponivel):
        pass

    def devolver(self, codigo, titulo, disponivel):
        
        pass
    

    def listarItens(self):
        return self.__itensLocados
    
    def locar(self, item: Item):
        if item.getDisponivel():
            item.alugar()
            self.__itensLocados.append(item)
            return True
        else:
            return False

    def devolver(self, item: Item):
        if item in self.__itensLocados:
            item.devolver()
            self.__itensLocados.remove(item)
            return True
        else:
            return False