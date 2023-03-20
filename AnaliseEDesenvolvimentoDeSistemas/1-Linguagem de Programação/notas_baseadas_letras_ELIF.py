nota = float(input('Qual a nota? '))
 
if nota >= 9:
    letra = 'A'
elif nota >= 8:
    letra = 'B'
elif nota >= 6:
    letra = 'C'
elif nota >= 4:
    letra = 'D'
else:
    letra = 'E'
 
print(f'Sua letra é: {letra}')
