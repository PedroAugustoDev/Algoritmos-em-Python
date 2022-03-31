'''
  Autor: Pedro Augusto
  Objetivo:  implemente um programa em Python que recebe um número real e informe se é igual a zero, 
  número positivo ou negativo.

  Nível Básico
'''

def propsNum(var1):
  if var1 == 0: return "O valor dado é igual a 0!"
  elif var1 > 0: return str(var1)+" é positivo!"
  else: return str(var1) + " é negativo!"


print(propsNum(-56.3))