# Algoritmo para demonstrar o funcionamento básico de 
# Uma simples Listas

# Diferente de outras linguagens, uma lista não é tipada
# O Que permite o armazenamento de diferentes tipos de dados na lista
# Darei o exemplo de uma lista de Coisas

# Notação simples
coisas = ["Fazer comida", "ir ao cinema", "comer"]
# Adicionando um elemento ao final da lista
coisas.append(1)
# A variavel index é a posição do novo item que irei adiconar
# não necessáriamente, eu armazenaria um novo elemento no final da lista,
# com o insert eu coloco onde eu quiser
# Com o index == 1, eu coloco na segunda posição
index = 1
coisas.insert(index, 33)

# Notação a partir da classe seria
# coisas = list()

# coisas é do tipo List
print(type((coisas)))
print(f'Lista de coisas: {coisas}')
# Imprimindo um elemento qualquer
# Lembre-se sempre, o index começa do 0
# pegando o segundo elemento
print('O segundo elemento é:', coisas[1])


# removendo por indice 
del coisas[1]
# ser olharmos a lista novamente, não teríamos mais o elemento 33
print(coisas)
# remoção com método
coisas.remove('comer')
print(coisas)

listaA = coisas
listaA[0] = "Pedro Augusto"
# É verdadeiro porque a lista não foi copiada, mas sim o endereço de memória
# Então se eu fazer isso uma alteração na lista, mudará as duas
print(coisas[0] == listaA[0])



# Copiando listas 
copia_lista = coisas[:]
copia_lista[0] = "Pedroca"
if copia_lista[0] == coisas[0]:
  print("A copia deu errado")
else: print("Cópia realizada com sucesso, as listas são diferentes")