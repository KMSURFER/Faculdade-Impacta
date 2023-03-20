pulo, qtd_canos = input().split()
pulo, qtd_canos = int(pulo), int(qtd_canos)

canos = input().split()

for i in range(len(canos)):
    canos[i] = int(canos[i])

i = 0
morreu = False
while i <= len(canos)-2:
    if canos[i] + pulo < canos[i+1]:
        print('GAME OVER')
        morreu = True
        break
    elif canos[i] - canos[i+1] > pulo:
        print('GAME OVER')
        morreu = True
        break
    i += 1

if morreu == False:
    print('YOU WIN')
