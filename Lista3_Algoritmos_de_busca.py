# Questão 1 - Refaça as funções de busca sequencial e busca binária assumindo que a lista possui chaves que podem ocorrer múltiplas vezes na lista. Neste caso, você deve retornar uma lista com todas as posições onde a chave foi encontrada. Se a chave não for encontrada na lista, retornar uma lista vazia.

def busca_sequencial_todas(lista, chave):
    posicoes = []
    for indice, numero in enumerate(lista):
        if numero == chave:
            posicoes.append(indice)
    return posicoes


def busca_binaria_todas(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    pos_encontrada = -1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            pos_encontrada = pos_meio
            break
        elif lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1

    if pos_encontrada == -1:
        return []

    posicoes = [pos_encontrada]

    esquerda = pos_encontrada - 1
    while esquerda >= 0 and lista[esquerda] == chave:
        posicoes.append(esquerda)
        esquerda -= 1

    direita = pos_encontrada + 1
    while direita < len(lista) and lista[direita] == chave:
        posicoes.append(direita)
        direita += 1

    posicoes.sort()
    return posicoes


lista_q1 = [5, 2, 8, 2, 9, 2, 1, 8]
lista_q1_ordenada = [1, 2, 2, 2, 5, 8, 8, 9]
print(busca_sequencial_todas(lista_q1, 2))
print(busca_binaria_todas(lista_q1_ordenada, 8))


# Questão 2 - Mostre como implementar uma variação da busca binária que retorne um inteiro k entre 0 e n, tal que, ou lista[k] = chave, ou a chave não se encontra na lista, mas poderia ser inserida entre as posições (k-1) e k de forma a manter a lista ordenada. Note que, se k = 0, então a chave deveria ser inserida antes da primeira posição da lista, assim como, se k = n, a chave deveria ser inserida após a última posição da lista.

def busca_insercao(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == chave:
            return pos_meio
        elif lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return pos_ini


lista_q2 = [1, 5, 15, 20, 24, 45, 67, 76, 78, 100]
print(busca_insercao(lista_q2, 15))
print(busca_insercao(lista_q2, 30))


# Questão 3 - Use a função desenvolvida acima para, dada uma lista ordenada de n números inteiros e distintos e dois outros inteiros X e Y, retornar o número de chaves da lista que são maiores ou iguais a X e menores ou iguais a Y.

def contar_no_intervalo(lista, X, Y):
    k1 = busca_insercao(lista, X)
    k2 = busca_insercao(lista, Y + 1)
    return k2 - k1


lista_q3 = [1, 5, 15, 20, 24, 45, 67, 76, 78, 100]
print(contar_no_intervalo(lista_q3, 10, 70))



# LISTA 3 - ALGORITMOS DE BUSCA EM PYTHON
# PARTE 1 - BUSCA SEQUENCIAL


# Questão 1 - Crie uma lista com 10 números inteiros e desenvolva um programa que solicite ao usuário um número. Utilize a busca sequencial para informar se o número está presente na lista.

lista1 = [4, 8, 15, 16, 23, 42, 7, 19, 31, 55]
numero1 = int(input("Digite um número: "))
encontrado1 = False
for i in range(len(lista1)):
    if lista1[i] == numero1:
        encontrado1 = True
        break
if encontrado1:
    print("O número está presente na lista.")
else:
    print("O número não está presente na lista.")


# Questão 2 - Dada uma lista de nomes, solicite um nome ao usuário e utilize a busca sequencial para informar a posição em que ele foi encontrado. Caso não exista, informe uma mensagem adequada.

nomes2 = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
nome2 = input("Digite um nome: ")
posicao2 = -1
for i in range(len(nomes2)):
    if nomes2[i] == nome2:
        posicao2 = i
        break
if posicao2 != -1:
    print("Nome encontrado na posição", posicao2)
else:
    print("Nome não encontrado na lista.")


# Questão 3 - Crie uma função busca_sequencial(lista, valor) que retorne o índice do valor procurado ou -1 caso ele não esteja presente.

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


lista3 = [10, 20, 30, 40, 50]
print(busca_sequencial(lista3, 30))
print(busca_sequencial(lista3, 100))


# Questão 4 - Dada uma lista de notas de alunos, solicite uma nota e verifique, por meio da busca sequencial, se ela aparece na lista. Informe também quantas vezes ela ocorre.

notas4 = [7.5, 8.0, 6.5, 9.0, 7.5, 5.0, 7.5]
nota4 = float(input("Digite uma nota: "))
ocorrencias4 = 0
for n in notas4:
    if n == nota4:
        ocorrencias4 += 1
if ocorrencias4 > 0:
    print("A nota", nota4, "aparece", ocorrencias4, "vez(es) na lista.")
else:
    print("A nota", nota4, "não aparece na lista.")


# Questão 5 - Crie uma lista de produtos e uma lista correspondente de preços. Solicite o nome de um produto e utilize busca sequencial para localizar o produto e exibir seu preço.

produtos5 = ["Arroz", "Feijão", "Macarrão", "Açúcar", "Café"]
precos5 = [22.90, 8.50, 5.30, 4.20, 15.00]
produto5 = input("Digite o nome do produto: ")
posicao5 = -1
for i in range(len(produtos5)):
    if produtos5[i] == produto5:
        posicao5 = i
        break
if posicao5 != -1:
    print("Preço de", produto5, ": R$", precos5[posicao5])
else:
    print("Produto não encontrado.")


# Questão 6 - Dada uma lista de números inteiros, utilize busca sequencial para localizar o maior valor sem utilizar as funções max() ou sort().

numeros6 = [34, 12, 89, 45, 67, 23, 90, 5]
maior6 = numeros6[0]
for numero in numeros6:
    if numero > maior6:
        maior6 = numero
print("O maior valor da lista é:", maior6)


# Questão 7 - Crie uma lista com números aleatórios. Solicite um valor e, usando busca sequencial, informe todas as posições em que esse valor aparece.

import random
lista7 = [random.randint(1, 50) for _ in range(15)]
print("Lista gerada:", lista7)
valor7 = int(input("Digite um valor para buscar: "))
posicoes7 = []
for i in range(len(lista7)):
    if lista7[i] == valor7:
        posicoes7.append(i)
if posicoes7:
    print("Valor encontrado nas posições:", posicoes7)
else:
    print("Valor não encontrado na lista.")


# Questão 8 - Desenvolva uma função que receba uma lista e um número e retorne True se o número existir na lista e False caso contrário. A função deve utilizar busca sequencial.

def contem_valor(lista, numero):
    for item in lista:
        if item == numero:
            return True
    return False


lista8 = [3, 6, 9, 12, 15]
print(contem_valor(lista8, 9))
print(contem_valor(lista8, 10))


# Questão 9 - Uma escola possui uma lista com os números de matrícula dos alunos. Solicite uma matrícula e verifique se o aluno está cadastrado utilizando busca sequencial.

matriculas9 = [1001, 1002, 1003, 1004, 1005]
matricula9 = int(input("Digite o número de matrícula: "))
cadastrado9 = False
for m in matriculas9:
    if m == matricula9:
        cadastrado9 = True
        break
if cadastrado9:
    print("Aluno cadastrado.")
else:
    print("Aluno não cadastrado.")


# Questão 10 - Dada uma lista de palavras, utilize busca sequencial para encontrar a palavra com maior quantidade de caracteres. Não utilize max() com chave.

palavras10 = ["casa", "computador", "sol", "biblioteca", "caneta"]
maior_palavra10 = palavras10[0]
for palavra in palavras10:
    if len(palavra) > len(maior_palavra10):
        maior_palavra10 = palavra
print("A palavra com mais caracteres é:", maior_palavra10)


# Questão 11 - Crie um programa que possua uma lista de CPFs fictícios. Solicite um CPF e informe se ele está cadastrado. Conte também quantas comparações foram necessárias até encontrá-lo.

cpfs11 = ["11122233344", "22233344455", "33344455566", "44455566677"]
cpf11 = input("Digite o CPF: ")
comparacoes11 = 0
encontrado11 = False
for c in cpfs11:
    comparacoes11 += 1
    if c == cpf11:
        encontrado11 = True
        break
if encontrado11:
    print("CPF cadastrado. Comparações realizadas:", comparacoes11)
else:
    print("CPF não cadastrado. Comparações realizadas:", comparacoes11)


# Questão 12 - Implemente uma busca sequencial que pare assim que encontrar o valor procurado. Exiba o valor encontrado, sua posição e o número de comparações realizadas.

lista12 = [12, 45, 67, 3, 89, 21, 56]
chave12 = 89
comparacoes12 = 0
posicao12 = -1
for i in range(len(lista12)):
    comparacoes12 += 1
    if lista12[i] == chave12:
        posicao12 = i
        break
if posicao12 != -1:
    print("Valor encontrado:", chave12)
    print("Posição:", posicao12)
    print("Comparações realizadas:", comparacoes12)
else:
    print("Valor não encontrado. Comparações realizadas:", comparacoes12)



# PARTE 2 - BUSCA BINÁRIA


# Questão 13 - Crie uma lista ordenada de números inteiros e implemente manualmente a busca binária para localizar um número informado pelo usuário.

lista13 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
numero13 = int(input("Digite um número para buscar: "))
pos_ini13 = 0
pos_fim13 = len(lista13) - 1
posicao13 = -1
while pos_ini13 <= pos_fim13:
    pos_meio13 = (pos_ini13 + pos_fim13) // 2
    if lista13[pos_meio13] == numero13:
        posicao13 = pos_meio13
        break
    elif lista13[pos_meio13] > numero13:
        pos_fim13 = pos_meio13 - 1
    else:
        pos_ini13 = pos_meio13 + 1
if posicao13 != -1:
    print("Número encontrado na posição", posicao13)
else:
    print("Número não encontrado na lista.")


# Questão 14 - Crie uma função busca_binaria(lista, valor) que receba uma lista ordenada e retorne o índice do valor procurado ou -1 caso ele não seja encontrado.

def busca_binaria(lista, valor):
    pos_ini = 0
    pos_fim = len(lista) - 1
    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if lista[pos_meio] == valor:
            return pos_meio
        elif lista[pos_meio] > valor:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return -1


lista14 = [5, 10, 15, 20, 25, 30, 35]
print(busca_binaria(lista14, 25))
print(busca_binaria(lista14, 100))


# Questão 15 - Dada uma lista ordenada de nomes, implemente uma busca binária para verificar se um nome informado pelo usuário está presente na lista.

nomes15 = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fabio"]
nome15 = input("Digite um nome para buscar: ")
pos_ini15 = 0
pos_fim15 = len(nomes15) - 1
encontrado15 = False
while pos_ini15 <= pos_fim15:
    pos_meio15 = (pos_ini15 + pos_fim15) // 2
    if nomes15[pos_meio15] == nome15:
        encontrado15 = True
        break
    elif nomes15[pos_meio15] > nome15:
        pos_fim15 = pos_meio15 - 1
    else:
        pos_ini15 = pos_meio15 + 1
if encontrado15:
    print("Nome presente na lista.")
else:
    print("Nome não presente na lista.")


# Questão 16 - Crie uma lista ordenada com 20 números. Realize uma busca binária e exiba, a cada iteração, os valores das variáveis inicio, fim e meio.

lista16 = list(range(2, 42, 2))
chave16 = 30
pos_ini16 = 0
pos_fim16 = len(lista16) - 1
while pos_ini16 <= pos_fim16:
    pos_meio16 = (pos_ini16 + pos_fim16) // 2
    print("inicio =", pos_ini16, "fim =", pos_fim16, "meio =", pos_meio16)
    if lista16[pos_meio16] == chave16:
        print("Valor encontrado na posição", pos_meio16)
        break
    elif lista16[pos_meio16] > chave16:
        pos_fim16 = pos_meio16 - 1
    else:
        pos_ini16 = pos_meio16 + 1
else:
    print("Valor não encontrado na lista.")


# Questão 17 - Dada uma lista ordenada de códigos de produtos, solicite um código e utilize busca binária para verificar se ele está cadastrado.

codigos17 = [101, 205, 309, 412, 517, 620, 733]
codigo17 = int(input("Digite o código do produto: "))
pos_ini17 = 0
pos_fim17 = len(codigos17) - 1
encontrado17 = False
while pos_ini17 <= pos_fim17:
    pos_meio17 = (pos_ini17 + pos_fim17) // 2
    if codigos17[pos_meio17] == codigo17:
        encontrado17 = True
        break
    elif codigos17[pos_meio17] > codigo17:
        pos_fim17 = pos_meio17 - 1
    else:
        pos_ini17 = pos_meio17 + 1
if encontrado17:
    print("Código cadastrado.")
else:
    print("Código não cadastrado.")


# Questão 18 - Modifique a busca binária para contar quantas comparações são necessárias para localizar um elemento.

lista18 = [3, 9, 15, 21, 27, 33, 39, 45]
chave18 = 27
pos_ini18 = 0
pos_fim18 = len(lista18) - 1
comparacoes18 = 0
posicao18 = -1
while pos_ini18 <= pos_fim18:
    pos_meio18 = (pos_ini18 + pos_fim18) // 2
    comparacoes18 += 1
    if lista18[pos_meio18] == chave18:
        posicao18 = pos_meio18
        break
    elif lista18[pos_meio18] > chave18:
        pos_fim18 = pos_meio18 - 1
    else:
        pos_ini18 = pos_meio18 + 1
if posicao18 != -1:
    print("Elemento encontrado na posição", posicao18)
else:
    print("Elemento não encontrado.")
print("Comparações realizadas:", comparacoes18)


# Questão 19 - Implemente uma busca binária que retorne True ou False, sem retornar o índice do elemento.

lista19 = [2, 4, 6, 8, 10, 12, 14]
chave19 = 10
pos_ini19 = 0
pos_fim19 = len(lista19) - 1
resultado19 = False
while pos_ini19 <= pos_fim19:
    pos_meio19 = (pos_ini19 + pos_fim19) // 2
    if lista19[pos_meio19] == chave19:
        resultado19 = True
        break
    elif lista19[pos_meio19] > chave19:
        pos_fim19 = pos_meio19 - 1
    else:
        pos_ini19 = pos_meio19 + 1
print(resultado19)


# Questão 20 - Dada uma lista ordenada contendo números pares de 2 até 200, utilize busca binária para localizar um número informado pelo usuário.

lista20 = list(range(2, 202, 2))
numero20 = int(input("Digite um número par entre 2 e 200: "))
pos_ini20 = 0
pos_fim20 = len(lista20) - 1
encontrado20 = False
while pos_ini20 <= pos_fim20:
    pos_meio20 = (pos_ini20 + pos_fim20) // 2
    if lista20[pos_meio20] == numero20:
        encontrado20 = True
        break
    elif lista20[pos_meio20] > numero20:
        pos_fim20 = pos_meio20 - 1
    else:
        pos_ini20 = pos_meio20 + 1
if encontrado20:
    print("Número encontrado na lista.")
else:
    print("Número não encontrado na lista.")


# Questão 21 - Crie uma lista ordenada com valores repetidos. Implemente uma busca binária capaz de localizar uma ocorrência do valor procurado e informe seu índice.

lista21 = [1, 3, 3, 3, 5, 7, 7, 9, 11]
chave21 = 7
pos_ini21 = 0
pos_fim21 = len(lista21) - 1
posicao21 = -1
while pos_ini21 <= pos_fim21:
    pos_meio21 = (pos_ini21 + pos_fim21) // 2
    if lista21[pos_meio21] == chave21:
        posicao21 = pos_meio21
        break
    elif lista21[pos_meio21] > chave21:
        pos_fim21 = pos_meio21 - 1
    else:
        pos_ini21 = pos_meio21 + 1
if posicao21 != -1:
    print("Valor encontrado no índice", posicao21)
else:
    print("Valor não encontrado.")


# Questão 22 - Desenvolva uma versão da busca binária que encontre a primeira ocorrência de um valor repetido em uma lista ordenada.

lista22 = [1, 3, 3, 3, 5, 7, 7, 9, 11]
chave22 = 3
pos_ini22 = 0
pos_fim22 = len(lista22) - 1
primeira_posicao22 = -1
while pos_ini22 <= pos_fim22:
    pos_meio22 = (pos_ini22 + pos_fim22) // 2
    if lista22[pos_meio22] == chave22:
        primeira_posicao22 = pos_meio22
        pos_fim22 = pos_meio22 - 1
    elif lista22[pos_meio22] > chave22:
        pos_fim22 = pos_meio22 - 1
    else:
        pos_ini22 = pos_meio22 + 1
if primeira_posicao22 != -1:
    print("Primeira ocorrência no índice", primeira_posicao22)
else:
    print("Valor não encontrado.")


# Questão 23 - Desenvolva uma versão da busca binária que encontre a última ocorrência de um valor repetido em uma lista ordenada.

lista23 = [1, 3, 3, 3, 5, 7, 7, 9, 11]
chave23 = 7
pos_ini23 = 0
pos_fim23 = len(lista23) - 1
ultima_posicao23 = -1
while pos_ini23 <= pos_fim23:
    pos_meio23 = (pos_ini23 + pos_fim23) // 2
    if lista23[pos_meio23] == chave23:
        ultima_posicao23 = pos_meio23
        pos_ini23 = pos_meio23 + 1
    elif lista23[pos_meio23] > chave23:
        pos_fim23 = pos_meio23 - 1
    else:
        pos_ini23 = pos_meio23 + 1
if ultima_posicao23 != -1:
    print("Última ocorrência no índice", ultima_posicao23)
else:
    print("Valor não encontrado.")


# Questão 24 - Dada uma lista ordenada de idades, utilize busca binária para verificar se uma idade específica está presente e informe quantos elementos foram descartados durante o processo.

idades24 = [15, 18, 21, 24, 28, 33, 40, 47, 55, 62]
idade24 = 33
pos_ini24 = 0
pos_fim24 = len(idades24) - 1
descartados24 = 0
encontrado24 = False
while pos_ini24 <= pos_fim24:
    pos_meio24 = (pos_ini24 + pos_fim24) // 2
    if idades24[pos_meio24] == idade24:
        encontrado24 = True
        break
    elif idades24[pos_meio24] > idade24:
        descartados24 += pos_fim24 - pos_meio24 + 1
        pos_fim24 = pos_meio24 - 1
    else:
        descartados24 += pos_meio24 - pos_ini24 + 1
        pos_ini24 = pos_meio24 + 1
if encontrado24:
    print("Idade encontrada na lista.")
else:
    print("Idade não encontrada.")
print("Elementos descartados:", descartados24)



# PARTE 3 - PROBLEMAS APLICADOS E COMPARAÇÃO


# Questão 25 - Sistema de Biblioteca: Uma biblioteca possui uma lista ordenada de códigos de livros. Implemente uma busca binária para verificar se um código informado está disponível. Caso esteja, informe a posição do livro na lista.

codigos_livros25 = [101, 205, 310, 415, 520, 625, 730, 835]
codigo_livro25 = int(input("Digite o código do livro: "))
pos_ini25 = 0
pos_fim25 = len(codigos_livros25) - 1
posicao25 = -1
while pos_ini25 <= pos_fim25:
    pos_meio25 = (pos_ini25 + pos_fim25) // 2
    if codigos_livros25[pos_meio25] == codigo_livro25:
        posicao25 = pos_meio25
        break
    elif codigos_livros25[pos_meio25] > codigo_livro25:
        pos_fim25 = pos_meio25 - 1
    else:
        pos_ini25 = pos_meio25 + 1
if posicao25 != -1:
    print("Livro disponível na posição", posicao25)
else:
    print("Código não encontrado.")


# Questão 26 - Controle de Estoque: Uma loja possui uma lista de produtos e deseja localizar um produto pelo código. Implemente uma solução com busca sequencial e outra com busca binária. Compare os resultados.

produtos_estoque26 = [102, 156, 189, 210, 245, 278, 301]
codigo_busca26 = 245

comparacoes_sequencial26 = 0
posicao_sequencial26 = -1
for i in range(len(produtos_estoque26)):
    comparacoes_sequencial26 += 1
    if produtos_estoque26[i] == codigo_busca26:
        posicao_sequencial26 = i
        break

pos_ini26 = 0
pos_fim26 = len(produtos_estoque26) - 1
comparacoes_binaria26 = 0
posicao_binaria26 = -1
while pos_ini26 <= pos_fim26:
    pos_meio26 = (pos_ini26 + pos_fim26) // 2
    comparacoes_binaria26 += 1
    if produtos_estoque26[pos_meio26] == codigo_busca26:
        posicao_binaria26 = pos_meio26
        break
    elif produtos_estoque26[pos_meio26] > codigo_busca26:
        pos_fim26 = pos_meio26 - 1
    else:
        pos_ini26 = pos_meio26 + 1

print("Busca sequencial -> posição:", posicao_sequencial26, "| comparações:", comparacoes_sequencial26)
print("Busca binária -> posição:", posicao_binaria26, "| comparações:", comparacoes_binaria26)


# Questão 27 - Cadastro de Alunos: Dada uma lista de matrículas, crie um programa que permita ao usuário escolher entre busca sequencial ou busca binária. Para a busca binária, garanta que a lista esteja ordenada.

matriculas27 = [1001, 1002, 1005, 1010, 1015, 1020, 1030]
opcao27 = input("Escolha o tipo de busca (sequencial/binaria): ")
matricula_busca27 = int(input("Digite a matrícula: "))

if opcao27 == "sequencial":
    posicao27 = -1
    for i in range(len(matriculas27)):
        if matriculas27[i] == matricula_busca27:
            posicao27 = i
            break
    if posicao27 != -1:
        print("Matrícula encontrada na posição", posicao27)
    else:
        print("Matrícula não encontrada.")
elif opcao27 == "binaria":
    lista_ordenada27 = sorted(matriculas27)
    pos_ini27 = 0
    pos_fim27 = len(lista_ordenada27) - 1
    posicao27 = -1
    while pos_ini27 <= pos_fim27:
        pos_meio27 = (pos_ini27 + pos_fim27) // 2
        if lista_ordenada27[pos_meio27] == matricula_busca27:
            posicao27 = pos_meio27
            break
        elif lista_ordenada27[pos_meio27] > matricula_busca27:
            pos_fim27 = pos_meio27 - 1
        else:
            pos_ini27 = pos_meio27 + 1
    if posicao27 != -1:
        print("Matrícula encontrada na posição", posicao27, "(lista ordenada)")
    else:
        print("Matrícula não encontrada.")
else:
    print("Opção inválida.")


# Questão 28 - Comparação de Desempenho: Crie uma lista ordenada com 1.000 números. Procure o último elemento usando busca sequencial e busca binária. Conte o número de comparações realizadas em cada algoritmo e apresente uma conclusão.

lista28 = list(range(1, 1001))
chave28 = 1000

comparacoes_sequencial28 = 0
for i in range(len(lista28)):
    comparacoes_sequencial28 += 1
    if lista28[i] == chave28:
        break

pos_ini28 = 0
pos_fim28 = len(lista28) - 1
comparacoes_binaria28 = 0
while pos_ini28 <= pos_fim28:
    pos_meio28 = (pos_ini28 + pos_fim28) // 2
    comparacoes_binaria28 += 1
    if lista28[pos_meio28] == chave28:
        break
    elif lista28[pos_meio28] > chave28:
        pos_fim28 = pos_meio28 - 1
    else:
        pos_ini28 = pos_meio28 + 1

print("Comparações na busca sequencial:", comparacoes_sequencial28)
print("Comparações na busca binária:", comparacoes_binaria28)
print("Conclusão: a busca binária localizou o elemento com muito menos comparações que a busca sequencial.")


# Questão 29 - Agenda Telefônica: Crie uma lista de contatos ordenada alfabeticamente. O usuário deve informar um nome e o programa deverá localizá-lo usando busca binária. Se encontrado, exiba também o telefone correspondente.

contatos29 = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fabio"]
telefones29 = ["1111-1111", "2222-2222", "3333-3333", "4444-4444", "5555-5555", "6666-6666"]
nome_busca29 = input("Digite o nome do contato: ")
pos_ini29 = 0
pos_fim29 = len(contatos29) - 1
posicao29 = -1
while pos_ini29 <= pos_fim29:
    pos_meio29 = (pos_ini29 + pos_fim29) // 2
    if contatos29[pos_meio29] == nome_busca29:
        posicao29 = pos_meio29
        break
    elif contatos29[pos_meio29] > nome_busca29:
        pos_fim29 = pos_meio29 - 1
    else:
        pos_ini29 = pos_meio29 + 1
if posicao29 != -1:
    print("Telefone de", nome_busca29, ":", telefones29[posicao29])
else:
    print("Contato não encontrado.")


# Questão 30 - Desafio: Crie um menu com as opções: (1) cadastrar valores, (2) exibir lista, (3) ordenar lista, (4) realizar busca sequencial, (5) realizar busca binária e (0) sair. A busca binária só poderá ser realizada quando a lista estiver ordenada.

lista30 = []
ordenada30 = False

while True:
    print("\n1 - Cadastrar valores")
    print("2 - Exibir lista")
    print("3 - Ordenar lista")
    print("4 - Busca sequencial")
    print("5 - Busca binária")
    print("0 - Sair")
    opcao30 = int(input("Escolha uma opção: "))

    if opcao30 == 1:
        valor30 = int(input("Digite um número para cadastrar: "))
        lista30.append(valor30)
        ordenada30 = False
    elif opcao30 == 2:
        print(lista30)
    elif opcao30 == 3:
        lista30.sort()
        ordenada30 = True
        print("Lista ordenada.")
    elif opcao30 == 4:
        valor30 = int(input("Digite o valor a buscar: "))
        posicao30 = -1
        for i in range(len(lista30)):
            if lista30[i] == valor30:
                posicao30 = i
                break
        if posicao30 != -1:
            print("Valor encontrado na posição", posicao30)
        else:
            print("Valor não encontrado.")
    elif opcao30 == 5:
        if not ordenada30:
            print("A lista precisa estar ordenada para a busca binária.")
        else:
            valor30 = int(input("Digite o valor a buscar: "))
            pos_ini30 = 0
            pos_fim30 = len(lista30) - 1
            posicao30 = -1
            while pos_ini30 <= pos_fim30:
                pos_meio30 = (pos_ini30 + pos_fim30) // 2
                if lista30[pos_meio30] == valor30:
                    posicao30 = pos_meio30
                    break
                elif lista30[pos_meio30] > valor30:
                    pos_fim30 = pos_meio30 - 1
                else:
                    pos_ini30 = pos_meio30 + 1
            if posicao30 != -1:
                print("Valor encontrado na posição", posicao30)
            else:
                print("Valor não encontrado.")
    elif opcao30 == 0:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")

# A busca sequêncial é mais adequada quando você possui poucos elementos para percorrer, já a busca binária, é mais adequada quando você possui um grande número de elementos.
# Com a lista ordenada, é possível utilizar a técnica de "dividir para conquistar" (achar o elemento pelo meio da lista), sendo assim, uma forma de busca muito eficiente.
