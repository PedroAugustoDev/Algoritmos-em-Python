

import math


var1 = float(input("Digite a largura da parede quadrada: "))
var2 = float(input("Digite a largura do azulejo: "))

def calc(size_wall, size_tile):
  wall_area = math.pow(size_wall, 2)
  tile_area = math.pow(size_tile, 2)
  return wall_area/tile_area





print(f'Em uma parede de {var1**2}cm\u00B2 cabem {calc(var1, var2)} azulejos de área igual a {var2**2}')

