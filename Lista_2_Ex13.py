# Questão 13. Valores acima da média
# Leia 10 números reais e armazene-os em uma lista. Calcule a média e depois exiba somente os valores que ficaram acima da média.
valores = []
for i in range(10):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    valores.append(valor)

print("Valores:", valores)

soma = 0
for valor in valores:
    soma += valor

media = soma / len(valores)
print(f"Média: {media:.2f}")

print("Valores acima da média:")
for valor in valores:
    if valor > media:
        print(valor)
