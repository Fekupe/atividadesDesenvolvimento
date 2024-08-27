n = int(input("Informe o número do qual quer saber a tabuada:"))
mult = 0

for _ in range (1,11):
    mult += 1
    resul = n * mult
    print (f"{n} X {mult} = {resul}")