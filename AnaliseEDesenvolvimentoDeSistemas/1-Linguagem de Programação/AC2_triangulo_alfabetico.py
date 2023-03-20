alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numero = int(input())


def mostra_letras_alfabeto(contador):
    numero_letra = alfabeto[contador - 1]

    i = 1

    while i <= contador:
        letras_alfabeto = numero_letra * contador
        i += 1

    print(letras_alfabeto)


if (1 <= numero <= 26):

    i = 1

    while i <= numero:
        mostra_letras_alfabeto(i)
        i += 1
