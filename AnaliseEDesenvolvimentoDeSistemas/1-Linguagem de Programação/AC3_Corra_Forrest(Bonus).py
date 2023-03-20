# 1 - VERSÃO #
# tempos = []
# soma = 0
# qtd = 0
# tempo = int(input())

# while tempo >= 0:
#     tempos.append(tempo)
#     soma += tempo
#     qtd += 1
#     tempo = int(input())

# media = soma / qtd
# print(f'MEDIA: {media:.2f}')

# for i in range(len(tempos)):
#     if tempos[i] < media:
#         print(tempos[i])

# 2 - VERSÃO #

# tempos = []

# tempo = int(input())

# while tempo >= 0:
#     tempos.append(tempo)
#     tempo = int(input())

# media = sum(tempos) / len(tempos)
# print(f'MEDIA: {media:.2f}')

# for tempo in tempos:
#     if tempo < media:
#         print(tempo)        

# 3- VERSÃO COM FUNCÃO #

def coleta_tempos():
    tempos = []
    tempo = int(input())
    while tempo >= 0:
        tempos.append(tempo)
        tempo = int(input())
    return tempos

def exibe_tempos(tempos, media): 
    for tempo in tempos:
        if tempo < media:
            print(tempo)    

tempos = coleta_tempos()
media = sum(tempos) / len(tempos)
print(f'MEDIA: {media:.2f}')
exibe_tempos(tempos, media)

 
