num_alunos = int(input("Qual o número de alunos?\n\t"))

while num_alunos < 3:
    num_alunos = int(input("Mínimo é 3... Qual o número de alunos?\n\t"))

alunos = []
notas = []

for i in range(num_alunos):
    nome = input(f"\nNome do aluno {i + 1}:\t")
    alunos.append(nome)
    nota = float(input(f"\nNota do aluno {i + 1}:\t"))
    notas.append(nota)

soma = sum(notas)
media = soma / num_alunos
print(f"\nA média geral é: {media}!")

maior_valor = max(notas)
posicao_maior = notas.index(maior_valor)
print(f"\nO aluno com maior nota é o {alunos[posicao_maior]} com {maior_valor}!")

menor_valor = min(notas)
posicao_menor = notas.index(menor_valor)
print(f"\nO aluno com menor nota é o {alunos[posicao_menor]} com {menor_valor}!")

alunos_acima_media = sum(1 for nota in notas if nota >= 6)
print(f"Número de alunos acima da média: {alunos_acima_media}")



