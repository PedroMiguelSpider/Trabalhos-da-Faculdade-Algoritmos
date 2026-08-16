# Questão 7. Busca de um elemento
# Leia 8 números e armazene-os em uma lista. Depois, solicite ao usuário um número para pesquisar. Informe se ele está ou não na lista. Não utilize index() para realizar a busca.
numeros = [12, 45, 7, 23, 89, 3, 56, 34]
print("Lista:", numeros)

numero_procurado = int(input("Digite o número que deseja procurar: "))

encontrado = False
for numero in numeros:
    if numero == numero_procurado:
        encontrado = True

if encontrado:
    print(f"O número {numero_procurado} está na lista.")
else:
    print(f"O número {numero_procurado} não está na lista.")
