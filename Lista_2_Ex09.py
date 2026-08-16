# Questão 9. Inserção e remoção
#Crie uma lista inicialmente vazia. Leia 5 números e utilize append() para inseri-los. 
# Depois, solicite um número ao usuário e remova sua primeira ocorrência, caso exista. Exiba a lista antes e depois da remoção.
lista = []
for i in range(5):
    valor = int(input(f"Digite o {i + 1}º número: "))
    lista.append(valor)

print("Lista:", lista)

numero_a_remover = int(input("Digite o número a ser removido: "))

if numero_a_remover in lista:
    lista.remove(numero_a_remover)

print("Lista depois da remoção:", lista)
