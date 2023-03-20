from paciente import Paciente, NameIsEmptyErro

try:
    nome = input('Digite o nomedo paciente: ')
    p = Paciente(nome)
except NameIsEmptyErro:
    print('O nome deve ser uma string, tente novamente...')
except NameIsEmptyErro:
    print('O nome não pode ser uma string, preencha um valor...')
except Exception as e:
    print('Ocorreu um erro inesperado ao criar o objeto de Paciente')
    print('informações de erro:', e)
else:
    print('se está aqui, não deu erro no try')
finally:
    print('sempre será executado!')
