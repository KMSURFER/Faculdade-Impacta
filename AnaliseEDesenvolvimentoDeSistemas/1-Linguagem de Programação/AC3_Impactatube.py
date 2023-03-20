# Montando a tabela #
# valor "lista" criado dentro da funcao "info_canal"       
def info_canal(lista):
  for _ in range(lista):
                                  # O ponto e virgula está pq o enunciado pede!#
    nome,inscritos,monetizacao,eh_cont_premium = input().split(';')

# Alterando o tipo de dados conforme informações #

    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    eh_cont_premium = eh_cont_premium == 'sim'

# Adicionando canal na lista de canais #
# comando ".append adiciona elemntos a lista" #
    canais.append([nome, inscritos, monetizacao, eh_cont_premium])

# funcao que cria e calcula a lista de bonificacao # 
# valor "valor_premium" e "valor_nao_premium" criado dentro da funcao "calcular_bonificacao"
# inicio da funcao #
def calcular_bonificacao(valor_premium, valor_nao_premium):
  lista_de_bonificacao = []

# ordenando os elementos dentro da lista e cria sua condicao de pagamento #
  for canal in canais:
    nome = canal[0]
    inscrito =canal[1]
    monetizacao = canal[2]
    eh_cont_premium = canal[3]   

    if(eh_cont_premium):
      monetizacao += inscrito // 1000 * valor_premium
    else:
      monetizacao += inscrito // 1000 * valor_nao_premium 

# adiciona "nome" e "monetizacao" na lista "lista_de_bonificacao"
    lista_de_bonificacao.append([nome, monetizacao])
# retorna lista_de_bonificacao    
  return lista_de_bonificacao
# fim da funcao "calcular_bonificacao"   

# criando funcao que exibe o bonus "exibir_bonificacao"
# inicio da funcao "exibir_bonificacao"
def exibir_bonificacao(bonus):
  print('-----')
  print('BÔNUS')
  print('-----')
# ordenando a lista bonificacao e imprimindo na tela #
  for bonificacao in bonus:
    nome = bonificacao[0]
    valor = bonificacao[1]
    print(f'{nome}: R$ {valor:.2f}')
# fim da funcao #    

canais = []

# entradas #
qtd_de_canais = int(input())

# condicao dada pelo enunciado #
if(1 <= qtd_de_canais <= 200):
  info_canal(qtd_de_canais)

  valor_premium = float(input())
  valor_nao_premium = float(input())

  exibir_bonificacao(calcular_bonificacao(valor_premium, valor_nao_premium))
