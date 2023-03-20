def exibe_nome():
    varíavel_local = 15
    print(f'O nome deste modulo é: {__name__!r}')


print('Olá')

nome = input('digite seu nome: ')


if __name__ == '__main__':
    exibe_nome()
