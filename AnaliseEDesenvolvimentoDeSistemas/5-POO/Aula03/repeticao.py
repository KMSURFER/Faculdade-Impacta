# Contagem de números de 0 a N

n = int(input('digite o numero: '))

cont = 0
while cont < n:
    print(cont)
    cont += 1

print('fim while')

for cont2 in range(n):
    print(cont2)

print('fim for')
