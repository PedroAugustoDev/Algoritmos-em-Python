# Exemplo de igualdade entre conjuntos

# Toda igualdade entre conjuntos deve obedecer o seguinte Postulado:
# A = B <=> (Ax)(x e A <=> x e B)

print("O seguinte postulado determina se A = B", "A = B \u27FA  para todo x (x \u20AC A \u27FA  x \u20AC B)", sep='\n')

A = set({'a','b'})
B = set({'b', 'c','d'})
C = set({'b', 'c', 'd', 'd'})

print(f'Conjunto A {A}')
print(f'Conjunto B {B}')
print(f'Conjunto C {C}\n')

print(f'O Conjunto A \u2260 B? {"Não" if A.__eq__(B) else "Sim"}')
print(f'O Conjunto B = C? {"Sim" if B.__eq__(C) else "Não"}')