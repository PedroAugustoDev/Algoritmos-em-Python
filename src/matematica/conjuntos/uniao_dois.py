

A = set({1,2,3,4})
B = set({1,4})

# A união B = A
print("A união B é igual a A" if A.union(B).__eq__(A) else A.union(B) )


C = set({1,2,3})
D = set({4,5,6})

print(C.union(D))



# criando um conjunto de 20 elementos
# N = {x e N| 1<= x <= 20}
N = set()
for i in range(1, 21):
  N.add(i)


print(N.union({1,2,33,44,5}))
