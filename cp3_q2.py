Temperaturas = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
i = 0
while i < 3:
    j = 0
    while j < 4:
        Temperaturas[i][j] = float(input(f"Temperatura da semana {i+1} e do dia {j+1}\n"))
        j = j+1
    i = i+1
for semana in Temperaturas:
    mediaSemana = sum(semana)/len(semana)
    print(f"A media da semana {i} é {mediaSemana}")
lista = [temperatura for linha in Temperaturas for temperatura in linha]
maiorNumero = max(lista)
menorNumero = min(lista)
mediaGeral = sum(lista)/len(lista)
print(f"O maior número é: {maiorNumero}")
print(f"O menor número é: {menorNumero}")
print(f"a media geral: {mediaGeral}")

