'''
 Autor: Pedro Augusto Lourenço Siqueira
 Objetivo: Mostrar a sequência de números de 1 até N
 sendo N, um valor passado pelo teclado, seja negativo ou positivo

 Nível: Básico
'''


def intervalo_de_um_n( n ):
   i = 1 
   while i <= n:
        print("valor: " + str(i))
        i = i + 1


def intervalo_de_um_n_negativo( n ):
    while n <= 1:
        print("valor: " + str(n))
        n = n + 1



def main():
    var1 = int(input("Digite um número interio: "))
    if var1 > 1: intervalo_de_um_n(var1)
    else: intervalo_de_um_n_negativo(var1)

main()