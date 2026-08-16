# Questão 10. Ordenação
# Considere numeros = [18, 5, 12, 3, 20, 7, 9]. Exiba a lista original, depois a lista em ordem crescente e finalmente em ordem decrescente. 
# Utilize sort() ou sorted() e explique, em comentário no código, a diferença entre eles.
numeros = [18, 5, 12, 3, 20, 7, 9]
print("Lista original:", numeros)


crescente = sorted(numeros)
print("Ordem crescente:", crescente)

decrescente = sorted(numeros, reverse=True)
print("Ordem decrescente:", decrescente)

print("Lista original:", numeros)
# lista.sort(): ordena a lista original in-place, e não retorna nada (retorna None).
# sorted(lista): cria e retorna uma nova lista ordenada, sem modificar a lista original. É melhor quando ainda for necessário usar a lista original (como no exercício)
# As duas funções aceitam o parâmetro reverse=True para retornar a ordem decrescente
