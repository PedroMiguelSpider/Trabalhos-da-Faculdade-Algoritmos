# Questão 2. Percorrendo uma lista
# Considere a lista numeros = [7, 12, 5, 18, 3, 20]. Percorra a lista e exiba cada elemento em uma linha. Depois, exiba somente os valores maiores que 10
numeros = [7, 12, 5, 18, 3, 20]
print("Todos os numeros:")
for numero in numeros:
    print(numero)

print("Valores maiores que 10:")
    for numero in numeros:
        if numero > 10:
            print(numero)
