# Sobrecarga

def sobrecarga(nome, numero=None):
    print(nome)
    if numero:
        print(numero)

print('primeira execução')
sobrecarga('kleber')

print ('\nsegunda execução')
sobrecarga('kleber', 10)
