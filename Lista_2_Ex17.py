# Questão 17. Segundo maior valor
# Dada uma lista de números inteiros, encontre o segundo maior valor distinto sem utilizar sort().
# Considere que a lista possui pelo menos dois valores distintos.
numeros = [23, 45, 12, 45, 67, 34, 67, 89, 5]
print("Lista:", numeros)

maior = float("-inf")
segundo_maior = float("-inf")

for numero in numeros:
    if numero > maior:
        segundo_maior = maior
        maior = numero
    elif numero > segundo_maior and numero != maior:
        segundo_maior = numero

print("Maior numero:", maior)
print("Segundo maior numero:", segundo_maior)
