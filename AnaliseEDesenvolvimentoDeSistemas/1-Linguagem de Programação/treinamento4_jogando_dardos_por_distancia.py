qtd = int(input())

for i in range(qtd):
    pj = 0
    for j in range(3):
        x, d = input().split()
        x, d = int(x), int(d)
        pj += x*d

    pm = 0
    for j in range(3):
        x, d = input().split()
        x, d = int(x), int(d)
        pm += x*d

    if pm > pj:
        print('MARIA')
    else:
        print('JOAO')
