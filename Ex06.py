# Questão 6 - Leia um número N e calcule a soma dos números de 1 até N.
n = int(input("Digite o valor de N: "))

soma = 0
for i in range(1, n + 1):
    soma_total += i

print(f"A soma de 1 até {n} é {soma_total}.")
