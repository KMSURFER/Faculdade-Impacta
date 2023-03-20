## Numero inserido pelo usuario ## 
numero = int(input())
## Condição dada pelo enunciado ##
if(0 <= numero <=10):
## Contador de tabuada do 1 , 2 , 3 ... 10##
    contador = 1
## comando de repetição WHILE ##
    while (contador <= 10):
## imprime na tela a tabuada desejada ##       
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1
