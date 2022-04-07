'''
  Autor: Pedro Augusto
  Implementação de um algoritimo de Produto Cartesiano
  Operação realizada entre conjuntos, formando pares

  Matemáticamente, um produto cartesiano pode ser descrito como
  AxB = {(x,y)| ∀x ∈ A ^ ∀y ∈ B}

  Nível: Simples - Porém Complexo na Matemática
'''


# Deve se passar conjuntos como argumentos dessa função
# Pois matematicamente, faz mais sentido.
def cartesiano(A, B):
  result = set()
  for x in A:
    for y in B:
      result.add(f'{x,y}')
  return result


