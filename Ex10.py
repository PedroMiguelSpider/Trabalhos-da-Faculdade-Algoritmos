# Questão 10 (Desafio) - Faça um programa que leia 5 números e informe o maior e o menor valor.
quantidade = 5

primeiro_valor = float(input("Digite o 1º número: "))
maior = primeiro_valor
menor = primeiro_valor

for i in range(1, quantidade):
    valor = float(input(f"Digite o {i + 1}º número: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
