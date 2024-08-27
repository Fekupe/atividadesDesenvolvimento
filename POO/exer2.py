class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def getinfo(self):
        return f"O nome do funcionário é {self.nome} e recebe um salário de {self.salario}R$"
        
    def aumentarSalario(self,percentualDeAumento):
        self.percentualDeAumento = percentualDeAumento
        return f"O salário era {self.salario}, com o aumento passou a ser {self.salario+self.salario*(percentualDeAumento/100)}, no caso, um aumento de {percentualDeAumento}% "
    
funcionario = Funcionario("Alexandre", 5000)
print(funcionario.getinfo())
print(funcionario.aumentarSalario(30))