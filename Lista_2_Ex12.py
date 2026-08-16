# Questão 12. Lista sem repetição
# Dada a lista numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10], crie uma nova lista contendo cada valor apenas uma vez, mantendo a ordem da primeira ocorrência. Não utilize set()
numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
print("Lista original:", numeros)

numeros_sem_repeticao = []
for numero in numeros:
    if numero not in numeros_sem_repeticao:
        numeros_sem_repeticao.append(numero)

print("Lista sem repetição:", numeros_sem_repeticao)
