
# Autor: Pedro Augusto
# Objetivo: Explicar parametros posicionais em Python



# Imaginamos que queremos utilizar muitos parametros
# De tal forma com que perdemssemos a ordem deles e para que eles servem
# por exemplo, imaginamos uma função onde, o primeiro valor é o nome e o segundo
# a idade, se invertessemos a ordem, ficaria errado se fissesemos isso:
# apresentar(19, "pedro")
# >> 19 e tenho pedro anos

# para evitar esses erros bobos, criou os parametros posicionais
# que é um novo jeito de se invocar funções. Veja agora:
# apresentar(idade=19, nome="pedro")
# >> Eu sou: pedro e tenho 19 anos

def apresentar(nome, idade):
  print(f'Eu sou: {nome} e tenho {idade} anos')


apresentar(19, "pedro")
apresentar(idade=19, nome="pedro")