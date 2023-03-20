def converte_2(f, sequencia):
    convertidos = []
    for item in sequencia:
        convertidos.append(f(item))
    return convertidos


def converte(tipo, sequencia):
    convertidos = []
    if tipo == "string":
        for item in sequencia:
            convertidos.append(str(item))
    elif tipo == "int":
        for item in sequencia:
            convertidos.append(int(item))
    elif tipo == "float":
        for item in sequencia:
            convertidos.append(float(item))
    else:
        raise Exception('tipo não reconhecido')

    return convertidos
