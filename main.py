import math

co = float(input('Insira o valor do Cateto Oposto: '))
ca = float(input('Insira o valor do Cateto Adjacente: '))

hip = math.sqrt((ca ** 2) + (co ** 2))

print(f'A hipotenusa desse dois números é {hip:.2f}')

sen = co/hip
cos = ca/hip
tan = co/ca

print(f'O valor do Seno é {sen:.2f};\n'
      f'O valor do Cosseno é {cos:.2f};\n'
      f'O valor da Tangente é {tan:.2f}')
