"""
Otimizaão para o Exercício 1, 2 e 3;
"""

v1 = int(input('Insira o Valor Inicial: '))
v2 = int(input('Insira o Valor Final: '))
v3 = int(input('Insira o Valor Contador: '))

while v3 == 0:
    print('O Contador não pode ser igual a Zero')
    v3 = int(input('Insira outro Valor: '))

if v3 > 0:
    x = v2+1
else:
    x = v2-1

for n in range(v1, x, v3):
    print(n)
