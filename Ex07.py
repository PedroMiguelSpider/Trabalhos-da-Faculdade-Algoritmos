# Questão 7 - Leia 10 números e informe a soma e a média.
soma = 0
quantidade = 10

for i in range(quantidade):
    num = float(input(f"Digite o {i + 1}º número: "))
    soma += num

media = soma / quantidade

print(f"A Soma dos números é: {soma}")
print(f"A Média dos números é: {media}")
