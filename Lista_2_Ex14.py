# Questão 14. Compreensão de listas
# Considere numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Crie, utilizando compreensão de listas: 
# Uma lista com os quadrados; uma lista somente com os pares; e uma lista contendo apenas os números maiores que 5.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = [n ** 2 for n in numeros]

pares = [n for n in numeros if n % 2 == 0]

maiores_que_5 = [n for n in numeros if n > 5]

print("Números:", numeros)
print("Quadrados:", quadrados)
print("Pares:", pares)
print("Maiores que 5:", maiores_que_5)
