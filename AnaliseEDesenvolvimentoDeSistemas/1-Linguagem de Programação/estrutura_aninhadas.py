idade = int(input('Qual a sua idade? '))                    #1
if idade >= 18:                                             #2
    cnh = input('Você tem CNH? (s/n)')                      #3
    if cnh == 's':                                          #4
        cnh_valida = input('Ela está válida? (s/n)')        #5
        if cnh_valida == 's':                               #6
            print('Você pode dirigir.')                     #7
        else:
            print('Você precisa renovar sua CNH.')          #8
    else:
        print('Você precisa tirar a CNH para dirigir.')     #9
else:
    print('Você ainda não pode dirigir.')                   #10 
    tempo_falta = 18 - idade                                #11
    if tempo_falta <= 2:                                    #12
        print('Falta pouco tempo para você poder dirigir.') #13
    else:
        print('Demorará para você poder dirigir.')          #14
    print('Mas você pode dirigir um kart se quiser.')       #15
print('Fim!')                                               #16
