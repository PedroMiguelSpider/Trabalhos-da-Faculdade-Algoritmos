# Questão 16. Lista de listas
# Crie uma matriz 3x3 utilizando listas de listas. Exiba todos os elementos, a soma de todos os valores e a soma de cada linha.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matriz:")
for linha in matriz:
    print(linha)  # [RESPOSTA] exibe cada linha da matriz

soma_total = 0
for linha in matriz:
    for valor in linha:
        soma_total += valor  # [RESPOSTA] soma todos os valores (loop duplo)

print("Soma de todos os valores:", soma_total)

print("Soma de cada linha:")
for linha in matriz:
    soma_linha = 0
    for valor in linha:
        soma_linha += valor  # [RESPOSTA] soma apenas os valores da linha atual
    print(soma_linha)
