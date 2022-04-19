'''
  Autor: Pedro Augusto Lourenço Siqueira
  Objetivo: Implementação de um algoritmo para
  reajuste do salário, acresentando 5, 10, 15% 
  de acordo com o salário.

  Nível: Básico
'''


SA = float(input('Digite seu salário atual: '))
NA = 0

if SA < 500: NA = SA + SA * .15
elif SA >= 500 and SA < 1000: NA = SA + SA * .10
else: NA = SA + SA * 0.05

print(f'O valor do salário novo é: {NA}')