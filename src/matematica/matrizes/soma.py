# Lib para operações matemáticas mais complexas
import numpy as np

a = np.matrix([[1,2,3], [4,5,6]])
b = np.matrix([ [0,0],[2,3], [1,1]])


c = np.matrix([[1,1], [1,1]])
'''        
MATRIX C = |1 1|
           |1 1|
           
'''




e = np.matrix([[1,2,3], [4,5,6], [7,8,9]])
f = np.matrix([[1,0,0],[0,1,0], [0,0,1]])

# A função dot serve para somar matrizes
print(e.dot(f))




