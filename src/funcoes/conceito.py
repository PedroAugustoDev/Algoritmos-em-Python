
# Autor: Pedro Augusto
# Objetivo: Explicar a estrutura básica de uma 
# função, mostrar para que serve e como se define uma



# toda função é estruturada com uma palavra chave
# no começo que é "def", em inglês define para definir uma função
# em seguida, colocaremos o nome e parenteses e dois pontos
# veja abaixo a definição função
def primeira_funcao():
  #corpo da função
  # essa função terá o objetivo de mosrtar "olá mundo na tela"
  print('olá Mundo')



# para invocar uma função, basta apenas por o nome dela
# seguido de seus parenteses, veja
primeira_funcao()
# será errado, você declarar uma função que ainda não exista
# isto é, chamar uma função antes de defini-la
# exemplo:

try:
  # eu ainda não defini a função chamada soma()
  # ou será dará erro
  soma()
except NameError:
  print("A função não existe ainda, então não podemos executá-la")

# mesmo criando a função soma, depois, dará erro.
# isto porque o Python interpreta o arquivo de cima para baixo
def soma():
  return 1 + 1