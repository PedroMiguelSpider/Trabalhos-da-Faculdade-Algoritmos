# Questão 15. Listas paralelas
# Crie duas listas: uma com 5 nomes de alunos e outra com suas respectivas notas.
# Percorra as listas simultaneamente e exiba o nome, a nota e a situação de cada aluno, considerando aprovação com nota maior ou igual a 6
nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
notas = [8.0, 5.5, 7.0, 4.0, 9.0]

for nome, nota in zip(nomes, notas):
    if nota >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f"{nome} - Nota: {nota} - Situação: {situacao}")
