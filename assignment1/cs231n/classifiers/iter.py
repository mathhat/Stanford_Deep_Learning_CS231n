
import numpy as np 
np.random.seed(1)
matrix = np.arange(1,26).reshape(5,5)
'''
it = np.nditer(matrix,flags=["multi_index"], op_flags=["readwrite"])
for i in range(10):
    print it.finished
    it.iternext()
'''
vec = np.random.randint(0,4,5)
print matrix
print vec
print matrix[range(5),vec]