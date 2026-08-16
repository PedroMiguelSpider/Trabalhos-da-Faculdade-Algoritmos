# Questão 5. Maior e menor valor
# Crie uma lista de números inteiros e determine o maior e o menor elemento sem utilizar max() ou min().
numeros = [23, 5, 67, 12, 89, 3, 45]

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
            maior = numero
    if numero < menor:
            menor = numero

print("Lista:", numeros)
print("Maior valor da lista:", maior)
print("Menor valor da lista:", menor)
