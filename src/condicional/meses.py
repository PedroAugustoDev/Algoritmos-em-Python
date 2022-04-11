'''
  Autor: Pedro Augusto 
  Fatec Ferraz 
  Objetivo: Estrutura de ifs encadeados
  para encontrar o mês a partir de um número 

'''

nmr_mes = int(input("Digite um número entre 1 e 12: "))
# deve se entrar com um valor entre 1 e 12
if nmr_mes > 0 and nmr_mes <= 12:
  # Com o operador end, podemos concatenar o valor do próximo print
  # de forma com que mostre dois dados com 1 linha.
  print('Valor válido, o mês escolhido foi:', end=' ')
  if nmr_mes == 1: print('Janeiro')
  elif nmr_mes == 2: print('Fevereiro')
  elif nmr_mes == 3: print('Março')
  elif nmr_mes == 4: print('Abril')
  elif nmr_mes == 5: print('Maio')
  elif nmr_mes == 6: print('Junho')
  elif nmr_mes == 7: print('Julho')
  elif nmr_mes == 8: print('Agosto')
  elif nmr_mes == 9: print('Setembro')
  elif nmr_mes == 10: print('Outubro')
  elif nmr_mes == 11: print('Novembro')
  elif nmr_mes == 12: print('Dezembro')
else: print('Valor inválido...')