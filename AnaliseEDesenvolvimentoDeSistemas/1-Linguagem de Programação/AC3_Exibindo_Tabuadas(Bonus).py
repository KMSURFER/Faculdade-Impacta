# a = int(input())
# b = int(input())

# if a <= b:
#     for multiplicando in range(a, b + 1):
#         for multiplicador in range(1, 11):
#             produto = multiplicando * multiplicador
#             print(f'{multiplicando} x {multiplicador} = {produto}')
#         print(10 * '-')
# else:
#     print('Nenhuma tabuada no intervalo!')

# Segunda forma de se construir usando função

def tabuada(multiplicando):
    for multiplicador in range(1, 11):
        produto = multiplicando * multiplicador
        print(f'{multiplicando} x {multiplicador} = {produto}')
    print(10 * '-')

a = int(input())
b = int(input())

if a <= b:
    for multiplicando in range(a, b + 1):
       tabuada(multiplicando)
else:
    print('Nenhuma tabuada no intervalo!')