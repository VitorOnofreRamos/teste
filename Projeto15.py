brancos = int(input('Insira o Total de votos brancos:'))
nulos = int(input('Insira o Total de votos nulos:'))
validos = int(input('Insira o Total de votos validos:'))

total = brancos + nulos + validos

brancos = brancos * 100 / total
nulos = nulos * 100 / total
validos = validos * 100 / total

print(f'O total de votos brancos foi {round(brancos, 2)}; \r\nO total de votos nulos foi {round(nulos, 2)}; \r\nO total de votos validos foram {round(validos, 2)}.')
