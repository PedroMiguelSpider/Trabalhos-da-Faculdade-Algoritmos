# Questão 8. Posição de um elemento
# Considere nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]. Solicite um nome ao usuário e informe a posição em que ele aparece. Caso não exista, informe que o nome não foi encontrado.
nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
print("Lista de nomes:", nomes)

nome_procurado = input("Digite o nome que deseja procurar: ")

posicao = -1
for indice, nome in enumerate(nomes):
    if nome == nome_procurado:
        posicao = indice

if posicao != -1:
    print(f"'{nome_procurado}' está na posição {posicao}.")
else:
    print(f"'{nome_procurado}' não foi encontrado.")
