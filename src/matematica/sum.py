# Program to sum two float's sum_numbers
# And sum all elements in list


var1 = float(input("Digite um número: "))
var2 = float(input("Digite um outro número: "))

def sum_numbers(x, y):
  return x + y


def sum_list(list_num):
  result = 0
  for i in range(len(list_num)):
    result += list_num[i]

  return result



print(f'A soma de {var1} com {var2} é igual a {sum_numbers(var1, var2)}')

