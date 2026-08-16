# Questão 11. Fatiamento
# Considere valores = [10, 20, 30, 40, 50, 60, 70, 80]. Utilizando slicing, exiba: os quatro primeiros elementos; os três últimos; os elementos das posições 2 a 5; e a lista invertida.
valores = [10, 20, 30, 40, 50, 60, 70, 80]
print("Lista original:", valores)

# Os quatro primeiros elementos
print("4 primeiros:", valores[:4])

# Os três últimos elementos
print("3 últimos:", valores[-3:])

# Elementos das posições 2 a 5
print("Posições 2 a 5:", valores[2:6])

# Lista invertida
print("Lista invertida:", valores[::-1])
