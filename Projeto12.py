ts = int(input('Insira um valor inteiro em segundos: '))

h = ts // 3600
m = (ts % 3600) // 60
s = (ts % 3600) % 60

print(f'{ts} equivale a {h} hora(s), {m} minuto(s) e {s} segundo(s).')
