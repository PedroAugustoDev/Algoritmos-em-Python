import numpy as np

a = np.matrix([[1,2],[0,5]])
b = np.matrix([[-1,1]])



# Para mostrar o resultado da multiplicação de matrizes
# Podemos printar o resultado chamando a função * __matmul__ * 

print(a.__matmul__(b))