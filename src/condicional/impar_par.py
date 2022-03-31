'''
  Autor: Pedro Augusto
  Objetivo: mplemente um programa em Python que recebe um número inteiro e informe se é par ou ímpar

  Nível Básico
'''


def impar_par(var1):
  if var1 % 2 == 0: return str(var1) + " é par!"
  else: str(var1) + " é impar!"


print(impar_par(4))