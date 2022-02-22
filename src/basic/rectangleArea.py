

# Return a list with first element is area
# and second is perimeter
def rectangle_props(width, height):
  area = width * height
  perimeter = (2 *width) + (2 * height)
  return [area, perimeter]


props = rectangle_props(5, 4)
print(f'Um retângulo de base:5 e altura: 4 tem o perímetro igual a: {props[1]}, e sua área é: {props[0]}')

