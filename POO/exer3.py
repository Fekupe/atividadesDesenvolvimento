class Livro:
    def __init__(self,nome,qtdPaginas,autor,preco):
        self.nome = nome 
        self.qtdPaginas = qtdPaginas
        self.autor = autor 
        self.preco = preco 

    def getPreco(self):
        return f"O preço do livro é {self.preco}R$"
    
    def setPreco(self,precoAtualizado):
        return f"O preço do livro recebeu uma atualização, sendo de {self.preco}R$ para {precoAtualizado}R$"
        

livro = Livro("Senhor dos Anéis", 1600, "J.R.R.Tolkien", 220)
print(livro.getPreco())
print(livro.setPreco(340))