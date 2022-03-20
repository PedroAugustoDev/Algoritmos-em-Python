'''
 Autor: Pedro Augusto Lourenço Siqueira
 Exemplo de intersecção de conjuntos
 Uma intersecção de conjuntos na matemática 
 é dada quando temos a criação de um novo conjunto 
 que recebe apenas os elementos que são iguais a dois conjuntos, isto é
 A∩B = {x| x∈A e x∈B}
'''


A = set({1,2,3,4})
B = set({2,4, 6})

# A∩B = {2,4}
print("A A∩BB =",A.intersection(B))
# A∩B = B∩A
print("São iguais" if A.intersection(B) == B.intersection(A) else "Impossivel ser diferente!")



# A união B intersecção A = A
# A uniao B = {1,2,3,4,6} 
# AuB∩A = {1,2,3,4} == A
print(A.union(B).intersection(A))