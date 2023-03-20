n = int(input())

def obter_notas():
    notas = []

    for i in range(n):
        notas.append(float(input()))

    return notas


def obter_notas_finais(notas_originais, novas_notas):
    quantidade_notas_alteradas = 0

    for i in range(len(notas_originais)):
        if (novas_notas[i] == 10 and notas_originais[i] < 10):
            novas_notas[i] = min(notas_originais[i] + 2, 10)
            quantidade_notas_alteradas += 1
        else:
            novas_notas[i] = novas_notas[i]

    return quantidade_notas_alteradas


def exibir_notas_alteradas(notas_originais, novas_finais, quantidade_notas_alteradas):
    print(f'NOTAS ALTERADADAS: {quantidade_notas_alteradas}')
    for i in range(n):
        nota_alterada = ('*' if notas_originais[i] != notas_finais[i] else '-')
        print(
            f'{nota_alterada}({i+1:03}) original: {notas_originais[i]:05.2f} | final {obter_notas_finais[i]:05.2f}')
