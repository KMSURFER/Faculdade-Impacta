def dobrar(x):
    return 2 * x


def triplicar(x):
    triplo = 3 * x
    return triplo


n1 = float(input('Digite um número:'))
dobro = dobrar(n1)
print(f'O Dobro é: {dobro}')
print(f'O Triplo é: {triplicar(n1)}')
