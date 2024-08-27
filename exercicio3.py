import random


num = int(input("Informe quantos números serão somados:"))
soma = 0
for _ in range (num):
    numale = random.randint(1,10) 
    soma += numale
    print(f"Números aleatórios: {numale}")

print(f"Soma total dos números aleatórios: {soma}")