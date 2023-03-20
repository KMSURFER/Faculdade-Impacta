texto = 'escrevendo a primeira frase'
with open('teste.txt', 'w') as f:
    f.write(texto)

s = [
    'linha 1',
    'linha 2',
    'linha 3',
    'linha 4'
]
with open('teste.txt', 'a') as f:
    f.writelines(s)

texto2 = 'escrevendo a primeira frase\n'
s2 = [
    'linha 1\n',
    'linha 2\n',
    'linha 3\n',
    'linha 4\n'
]

with open('teste2.txt', 'w') as f:
    f.write(texto2)
    f.writelines(s2)

with open('print.txt', 'w') as f:
    print(texto, file=f)
    for linha in s:
        print(linha, file=f)
