

# parametro @number indica qualquer número
# e a partir dele será imprimido no console sua tabuada
def tabuada( number ):
  i = 1
  while i <= 10:
    print(f'{i} x {number} = {i * number}')
    i += 1
  


tabuada(int(input("Digite qualquer número para se extrair sua tabuada: ")))