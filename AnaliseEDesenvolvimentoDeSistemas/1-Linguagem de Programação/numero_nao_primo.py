# Crie um programa que receba dois números naturais e exiba uma 
# mensagem indicando se o primeiro não é divisível pelo segundo.
 
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
print(f'{a} não é divisível por {b}: {b == 0 or a % b != 0}')
