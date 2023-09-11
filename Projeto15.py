brancos = int(input('Insira o Total de votos brancos:'))
nulos = int(input('Insira o Total de votos nulos:'))
validos = int(input('Insira o Total de votos validos:'))

total = brancos + nulos + validos / 100
brancos = total - brancos / 100
nulos = total - nulos / 100
validos = total - validos / 100

print(f'O total de votos brancos foi {brancos}; \r\nO total de votos nulos foi {nulos}; \r\nO total de votos validos foram {validos}.')
