
# Importando a lib Math para pegar o valor
# exato do pi, bem como, a lib os para limpar a tela

import math
import os 

os.system('cls')

def calc_area(r):
  area = math.pi * (math.pow(r, 2))
  return area