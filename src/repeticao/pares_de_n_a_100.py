'''
 Autor: Pedro Augusto Lourenço Siqueira
 Objetivo: Mostrar número pares maiores que 100 até 100 a partir de um número do capturado no teclado

 Nível: Básico
'''


def print_par_ate_100( number ):
    if number >= 100:
        while number >= 100:
            if number % 2 == 0: print(f'{number} é par')
            number -=1
    elif number == 100: print(number)
    else: print("O menor valor possível é 100, digite 100 ou um número maior")



print_par_ate_100(int(input("Diite um número a partir de 100 para descobrir os pares até 100: ")))