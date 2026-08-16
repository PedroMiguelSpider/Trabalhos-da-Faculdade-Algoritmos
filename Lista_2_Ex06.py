# Questão 6. Contagem de pares e ímpares
# Dada uma lista com 10 números inteiros, conte quantos são pares e quantos são ímpares. Exiba as duas quantidades ao final.
numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print("Lista:", numeros)
print("Quantidade de numeros pares:", pares)
print("Quantidade de numeros ímpares:", impares)
