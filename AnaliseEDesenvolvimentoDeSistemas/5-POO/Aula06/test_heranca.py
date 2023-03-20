from heranca import Mae, Filha, Neta

print('Criando objeto Mae...')
mae = Mae(1)

print('\nCriando objeto Filha...')
filha = Filha(1, 2)

print('\nCriando objeto Neta...')
neta = Neta(1, 2, 3)

print('\nVisualizando os objetos')
print('mae', vars(mae))
print('filha', vars(filha))
print('neta', vars(neta))
