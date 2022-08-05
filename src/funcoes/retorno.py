
# Autor: Pedro Augusto
# Objetivo: Explicar o que é a palavra chave return


# A palavra chave return, é na verdade um jeito que temos
# de retorar valores de dentro de uma função. Assim como na matemática
# onde passamos uma variável x e ganhamos um y, na programação também temos isso
# imagine uma função que associe um número ao seu quadrado, exemplo
# f(x) =  x^2, isto é uma função matematica que retorna o valor de x * x
# Em python, teríamos isso:

def f(x):
  return x*x
  # depois de um retorno, a função é a bandonada. Semelhante ao break do for
  # porem, retorna um valor, seja, int, float, string, None e etc


# podemos armazenar esse valor em uma variavel
p = f(5)
# podemos apenas mostrar o valor
print(f(5))
print(p)