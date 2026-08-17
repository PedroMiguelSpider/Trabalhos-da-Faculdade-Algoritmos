# Questão 20. Problema real — Análise de vendas
# Uma empresa registrou as vendas de uma semana na lista vendas = [1250, 980, 1430, 2100, 1750, 890, 1620].
# Desenvolva um programa que calcule o total vendido, a média diária, a maior e a menor venda, quantos dias ficaram acima da média e o percentual de dias acima da média.

vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]
print("Vendas da semana:", vendas)

total = 0
for venda in vendas:
    total += venda
print("Total vendido:", total)

media = total / len(vendas)
print(f"Média diária: {media:.2f}")

maior_venda = vendas[0]
menor_venda = vendas[0]
for venda in vendas:
    if venda > maior_venda:
        maior_venda = venda
    if venda < menor_venda:
        menor_venda = venda
print("Maior dia de venda:", maior_venda)
print("Menor dia de venda:", menor_venda)

dias_acima_da_media = 0
for venda in vendas:
    if venda > media:
        dias_acima_da_media += 1
print("Dias acima da média de vendas:", dias_acima_da_media)

percentual = (dias_acima_da_media / len(vendas)) * 100
print(f"Percentual de dias acima da média: {percentual:.2f}%")
