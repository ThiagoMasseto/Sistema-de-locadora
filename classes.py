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
    def cadastrarCliente(self):
        pass
    def cadastrarItem(self):
        pass
    def listarCliente(self):
        pass
    def listarItem(self):
        pass
        
class Item:
    def __init__(self, codigo, titulo, disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__disponivel = disponivel

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
    
    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel
        return disponivel
    #-------------------------------------------
    
    def alugar(self,):
        pass

    def devolver(self,):
        pass

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
#------------------------------------------------

class Cliente:
    def __init__(self, nome, cpf, itensLocados):
        self.__nome = nome
        self.__cpf= cpf
        self.__itensLocados= itensLocados

    #Metodos Gets e Sets
    def getNome(self):
        return self.__nome
    
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
    
    def locar():
        pass

    def devolver():
        pass

    def listarItens():
        pass
     