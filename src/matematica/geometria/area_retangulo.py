

'''
  Retorna uma lista onde:
  primeiro elemento é a área
  segundo elemento é o perimetro
'''

def rectangle_props(width, height):
  area = width * height
  perimeter = (2 *width) + (2 * height)
  return [area, perimeter]


base = 5
altura = 4

props = rectangle_props(base, altura)
print(f'Um retângulo de base: {base} e altura: {altura} tem o perímetro igual a: {props[1]}, e sua área é: {props[0]}')

