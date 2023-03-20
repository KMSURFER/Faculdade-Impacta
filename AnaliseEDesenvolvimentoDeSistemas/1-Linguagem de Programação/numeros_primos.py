# Crie um programa que receba dois números naturais e exiba uma 
# mensagem indicando se o primeiro é divisível pelo segundo.
 
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
print(f'{a} é divisível por {b}: {b != 0 and a % b == 0}')
