class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC) -> None:
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calculaPerimetro (self):
        return f"O Perímetro do Triângulo informado é : ({self.ladoA + self.ladoB + self.ladoC})"
    
    def getMaior (self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            return f"O lado A {self.ladoA} é o maior"
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            return f"O lado B {self.ladoB} é o maior"
        elif self.ladoC > self.ladoA and self.ladoC > self.ladoB:
            return f"O lado C {self.ladoC} é o maior"
        else:
            return "Os lados dos triângulo são iguais"

triangulo = Triangulo(15, 22, 33)
print(triangulo.calculaPerimetro())
print(triangulo.getMaior())