# Questão 4. Média de uma lista
# Considere notas = [7.5, 8.0, 6.0, 9.5, 5.5]. Calcule a média manualmente, percorrendo a lista. Ao final, informe a média com duas casas decimais
notas = [7.5, 8.0, 6.0, 9.5, 5.5]

soma = 0
for nota in notas:
    soma = soma + nota

    media = soma / len(notas)

print("Notas:", notas)
print(f"Média das notas: {media:.2f}")
