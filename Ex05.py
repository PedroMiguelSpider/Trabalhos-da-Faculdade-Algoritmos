# Questão 5 - Leia um número inteiro e mostre sua tabuada de 1 a 10.
numero = int(input("Digite um número inteiro para ver a sua tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
