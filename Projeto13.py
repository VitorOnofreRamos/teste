nfrangos = int(input('Isira o número de Frangos em sua Fazenda: '))

anel1 = 0.40
anel2 = 0.35

total = nfrangos * (anel1 + anel2 * 2)

#print(f'O total que vc irá gastar é {round(total, 2)} reais')
print(f'O total que vc irá gastar é {total:.2f} reais')
