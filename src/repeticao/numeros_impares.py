'''
  Autor: Pedro Augusto Lourenço Siqueira
  Objetivo: Mostrar os números pares postitivos de 
  uma posição inicial a uma final

  Nível Básico
'''



def mostrar_pares(start, len):
    while start <= len:
        if start % 2 != 0: print(f'{start} é impar')
        start +=1


var1 = int(input("Digite um número para começar o laço: "))
var2 = int(input("Digite um número para encerrar o laço: "))
mostrar_pares(var1, var2)