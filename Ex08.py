# Questão 8 - Leia vários números até que o usuário digite 0. Ao final, informe a soma dos valores digitados.
soma = 0
numero = float(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero
    numero = float(input("Digite um número (0 para parar): "))

print(f"Soma total dos valores digitados: {soma}")
