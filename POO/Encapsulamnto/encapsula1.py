class Produto:
    qtdProduto = 0
    def __init__(self, codigo, preco):
        self.__codigo = codigo
        self.__preco = preco
        Produto.qtdProduto += 1

    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        self.__preco = preco
        return self.__preco
    
    def getCodigo(self):
        return self._Produto__codigo
    
    def setCodigo(self, codigo):
        self._Produto__codigo = codigo
        return self._Produto__codigo

class GerenciadorProdutos:
    listaprodutos = []
    def __init__(self):
        self.listaprodutos = []
        

    def adicionaProdutos(self, prod):
        self.listaprodutos.append(prod)
        print("Produto adicionado com sucesso")
        return self.listaprodutos

    def removeProduto(self, codProduto):
        for pro in self.listaprodutos:
            if codProduto == pro.getCodigo():
                self.listaprodutos.remove(pro)
                print("Produto removido com sucesso")

    def precoTotal(self, listaCodigos):
        precoTotal = 0
        for cod in listaCodigos:
            for pro in self.listaprodutos:
                if cod == pro.getCodigo():
                    precoTotal += pro.getPreco()
        return precoTotal

produto = Produto(12, 123)
produto2 = Produto(9, 321)
produto3 = Produto(6, 456)
listapro = []

gerenciador = GerenciadorProdutos()

gerenciador.adicionaProdutos(produto)
gerenciador.adicionaProdutos(produto2)

gerenciador.removeProduto(12)
gerenciador.removeProduto(9)


