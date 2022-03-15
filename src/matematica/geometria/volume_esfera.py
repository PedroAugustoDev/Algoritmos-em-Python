
import math


def volume_esfera(ratio):
   v = 4/3 * (math.pi * (math.pow(ratio, 3)))
   return int(v)


print(f'o volume da esfera de raio {5} é \u2243 {volume_esfera(5)}')

