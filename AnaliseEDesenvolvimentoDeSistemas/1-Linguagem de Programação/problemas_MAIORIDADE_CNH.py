idade = int(input('Qual a sua idade? '))  # executado sempre
 
if idade >= 18:
    # Bloco executado quando a condição resulta verdadeiro
    print('Você pode ter uma CNH.')
    print('Desejamos boa sorte!')
else:
    # Bloco executado quando a condição resulta falso
    print('Você ainda não completou 18 anos, ', end='')
    print('portanto não pode ter uma CNH.')
 
print('Fim')  # executado sempre
