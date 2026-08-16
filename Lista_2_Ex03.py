# Questão 3. Soma dos elementos
# Crie uma lista com 8 números inteiros. Calcule e exiba a soma de todos os elementos sem utilizar a função sum().
numeros = [4, 8, 15, 16, 23, 42, 5, 9]

soma = 0
for numero in numeros:
    soma = soma + numero

print("Lista:", numeros)
print("Soma dos elementos (sem sum()):", soma)
