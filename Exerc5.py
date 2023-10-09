alunos = int(input('Quantidade de alunos: '))
notas = int(input('Quantidade de notas: '))

for i in range(alunos):
    soma = 0
    for n in range(notas):
        nota = float(input('Informe as nota: '))
        soma += nota
    media = soma / notas
    print(f'Media: {media:.2f}')
