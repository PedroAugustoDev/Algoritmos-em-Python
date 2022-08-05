
# Autor: Pedro Augusto
# Objetivo: Mostrar uma utilidade das funções
# Que são variaveis de escopo local, que servem 
# como porta de acesso dos dados ao interior da função


# exemplo
# uma função que soma dois argumentos e imprime na tela
def soma(x, y):
  print(x + y)

# os parametros, são variaveis que ficam dentro dos parenteses
soma(1, 2)
# a = 1 e b = 2
# note que e um erro chamar funções parametizadas sem passar seus parametros