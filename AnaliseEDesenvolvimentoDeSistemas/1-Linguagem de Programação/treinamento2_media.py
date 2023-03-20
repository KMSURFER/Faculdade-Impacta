n1 ,n2 ,n3 ,n4 = input().split() 

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5.0:
        print(f'Media: {media:.1f}')  
        print('Aluno reprovado.')
else:
    media >= 5.0 and media <= 6.9
    n5 = float(input())
    media_final = (n5 + media) / 2
    print(f'Media: {media:.1f}') 
    print('Aluno em exame.')
    print(f'Nota do exame: {n5:.1f}')

    if media_final >= 5.0:
            print('Aluno aprovado.')
            print(f'Media final: {media_final:.1f}')
    else:
            print('Aluno reprovado.')
            print(f'Media final: {media_final:.1f}')
    
