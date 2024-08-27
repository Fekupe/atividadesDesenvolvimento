import math
#Exercicio 1 (Faça um Programa que peça dois números e imprima a soma)
# a = int(input("Informe um número para somar: "))
# b = int(input("informe um segundo número para somar: "))
# soma = a+b
# print(f"O resultado da soma é: {soma}")

#Exercicio 2 (Faça um Programa que peça as 4 notas bimestrais e mostre a média)
# a = float(input("Informe a primeira nota: "))
# b = float(input("Informe a segunda nota: "))
# c = float(input("Informe a terceira nota: "))
# d = float(input("Informe a quarta nota: "))
# result = a+b+c+d
# media = result/4

# print(f"O resultado da média é: {media}")
# if media< 6:
#     print("Aluno está reprovado.")
# else:
#     print("Aluno está aprovado.")

#Exercicio 3 (Faça um Programa que converta metros para centímetros.)
# a = int(input("Informe em metros o que deseja converter: "))
# b = a*100
# print(f"O resultado da conversão é: {b}cm")

#Exercicio 4 (Faça um Programa que peça o raio de um círculo, calcule e mostre sua área)
# a = float(input("Informe o tamanho do raio do círculo: "))
# b = a**2
# c = 3.14
# d = c*b
# print(f"Assumindo que PI seja o valor padrão de 3.14 o resultado da área do círculo é: {d}")

#Exercicio 5 (Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.)
# a = int(input("Informe o tamanho do lado do quadrado: "))
# b = a**2
# c = b*2
# print(f"Dada o lado quadrado, temos respectivamente sua área: {b}, e o dobro da mesma {c}")

#Exercicio 6 (Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.)
# a = int(input("Informe qual o valor recebido por hora trabalhada: "))
# b = int(input("Informe quantas horas você trabalha: "))
# c = a*b
# print(f"O seu salário de acordo com o valor da hora e horas trabalhadas é no mês é: {c}")

#Exercicio 7 (Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. a. C = 5 * ((F-32) / 9).)
# a = float(input("Informe a temperatura em Fahrenheit: "))
# b = a - 32
# c = b/9
# d = 5*c
# print(f"O resultado da conversão de Fahrenheit para Celsius é: {d}")

#Exercicio 8 (Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.)
# a = float(input("Informe a temperatura em Celsius: "))
# b = a/5
# c = b*9
# d = c+32
# print(f"O resultado da conversão de Celsius para Fahrenheit é: {d}")

#Exercicio 9 (Faça um Programa que peça dois números e imprima o maior deles.)
# a = int(input("Informe um número: "))
# b = int(input("informe um segundo número: "))
# if a > b:
#     print(f"O maior número é: {a}")
# elif a==b:
#     print(f"Os números são iguais")
# else: 
#     print(f"O maior número é: {b}")

#Exercicio 10 (Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.)
# a = int(input("Informe um valor: "))
# if a > 0:
#     print(f"{a} é positivo.")
# elif a==0:
#     print(f"{a} é um número neutro.")
# else:
#     print(f"{a} é negativo.")

#Exercicio 11 (Faça um Programa que verifique se uma letra digitada é "F" ou "M".Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.)
# a = str(input("Informe uma letra entre as opções F ou M: "))
# if a == "F":
#     print("Você selecionou Feminino.")
# elif a== "M":
#     print("Você selecionou Masculino.")
# else:
#     print("Sexo indefinido.")

#Exercicio 12 (Faça um Programa que verifique se uma letra digitada é vogal ou consoante)
# a = input("Informe uma letra para saber se a mesma é vogal ou consoante: ")
# vogais = ["a", "e", "i", "o", "u"]
# if a in vogais:
#     print(f"{a} é uma vogal.")
# else:
#     print(f"{a} é uma consoante.")


#Exercicio 13 (Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; b. A mensagem "Reprovado", se a média for menor do que sete; c. A mensagem "Aprovado com Distinção", se a média for igual a dez.)
# a = float(input("Informe a primeira nota do aluno: "))
# b = float(input("Informe a segunda nota do aluno: "))
# c = a+b
# media = c/2
# if media == 10:
#     print("O aluno está aprovado com distinção.")
# elif 10 > media >= 7:
#     print("O aluno está aprovado.")
# elif media < 7:
#     print("O aluno está reprovado.")
# elif media < 0:
#     print("Informe um número positivo.")
# elif media > 10:
#     print("Informe um números entre 0 a 10.")

#Exercicio 14 (Faça um programa que leia e valide as seguintes informações: a. Nome: maior que 3 caracteres; b. Idade: entre 0 e 150; c. Salário: maior que zero; d. Sexo: 'f' ou 'm'; e. Estado Civil: 's', 'c', 'v', 'd'.)
# nome = str(input("Informe seu nome: "))
# idade = int(input("Informe sua idade: "))
# salario = float(input("Informe seu salário: "))
# sexo = str(input("Informe entre 'F' ou 'M': "))
# ecivil = str(input("Informe seu estado civil entre (S, C, V, D): "))
# estadoscivis = ['S', 'C', 'V', 'D']
# sexos = ['F', 'M']

# if len(nome) < 3:
#     nome = str(input("Informe um nome com mais de 3 caracteres:"))
# elif idade < 0:
#     idade = str(input("Informe uma idade entre 0 e 150 anos: "))
# elif idade > 150:
#     idade = str(input("Informe uma idade entre 0 e 150 anos: "))
# elif salario < 0:
#     idade = str(input("Informe um salário superior a 0: "))
# elif sexo not in sexos:
#     idade = str(input("Informe F ou M para o sexo: "))
# elif ecivil not in estadoscivis:
#     idade = str(input("Informe um Estado Civil entre as opções: "))
# else:
#     print(f"Seu nome é {nome}, tem {idade} anos, recebe {salario} de salário, se identifica com {sexo} e seu atual estado civil é {ecivil}")

#Exercicio 15