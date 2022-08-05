


def soma_enquanto_positivo():
  result = 0
  valor = 0
  while valor > -1:
    var1 = int(input("Digite um número: "))
    if var1 < 0: break
    else: valor = var1
    result += valor
  print(f"O resultado final da soma foi de: {result}")



soma_enquanto_positivo()