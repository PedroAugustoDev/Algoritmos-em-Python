'''
  Autor: Pedro Augusto
  Objetivo: implemente um programa Python que recebe dois números inteiros e mostre o 
  resultado da divisão deles. Se o segundo número é igual a zero, informe que é 
  impossível devido à divisão por zero.

  Nível Básico

'''


def division(var1, var2):
  if var2 == 0: return "É impossível dividir por 0"
  else: 
    result = var1/var2
    return str(var1)+" dividido por "+str(var2)+" é igual a: " + str(int(result) if result % 1 == 0 else result)



print(division(6.02E23,6.02E18))