
# a = 15
# b = -10
# c = 0
# if a > 0:
#     print("A eh maior que 0")
# elif a < 0:
#     print("A eh menor que zero")
# else:
#     print("A eh igual a zero")
# if b > 0:
#     print("B eh maior que 0")
# elif b < 0:
#     print("B eh menor que zero")
# else:
#     print("B eh igual a zero")
# if c > 0:
#     print("C eh maior que 0")
# elif c < 0:
#     print("C eh menor que zero")
# else:
#     print("C eh igual a zero")
#-----------------------------------------------------------------
num = float(input("Informe um numero:"))
if num > 0:
    print(num, "eh maior que zero")
elif num < 0:
    print(num, "eh menor que zero")
elif num == 0:
    print(num, "eh igual a zero")
else:
    print("Nao eh um numero")