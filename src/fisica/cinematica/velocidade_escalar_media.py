
#  Autor: Pedro Augusto Lourenço Siqueira
#  Objetivo: Programa para realizar cálculos de cinemática
#  simples, sem cálculo integral ou diferencial, apenas a 
#  matemática linear
import os


# limpar a tela do console
def clear():
  os.system('cls')


# Método para calcular a velocidade escalar média de um móvel em função
# da distância pelo tempo
#
# vem = Δd / Δt
def velocidade_e_media(Δd, Δt):
  return Δd/Δt


# Método para calcular a distância percorrida por um móvel
# em função de tempo e velocidade
# d = vem * Δt
def distancia_percorrida(vem, Δt):
  return vem * Δt


# Método para calcular a variação do tempo percorrida por um móvel
# em função da velocidade e da distância
# Δt = d/v
def variacao_tempo(d, v):
  return d/v


# Dado o seguinte problema
#  Um móvel percorreu um trjeto ABCD, no sentido de A para D.
#  No primeiro trecho AB, ele demorou 30min (50km), no segundo, BC, 
#  demorou 1h e a velocidade média foi de 60km/h. no Trecho CD foi com 80km/h
#  a uma distancia de 40km. Determine a velocidade escalar média de todo o
#  percurso, desde A até D.
#


clear()
result = velocidade_e_media((50 + distancia_percorrida(60, 1) + 40), (.5 + variacao_tempo(40, 80) + 1))
print(f'A velocidade escalar média do percurso foi de {result}km/h')