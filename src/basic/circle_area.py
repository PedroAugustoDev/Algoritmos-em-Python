# import math module to get PI value
import math

def calc_area(r):
  area = math.pi * (math.pow(r, 2))
  return area


# Print on precision of 2 decimals
print(f'A área de um circulo de raio 5cm é {round(calc_area(5),2)}cm\u00B2')