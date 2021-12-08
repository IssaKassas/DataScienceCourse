
# # converting from 5dm -> m : 5/10
# # dm^3 = 1 liter
# # 1 liter => 1dm^3 => 1/1000 m^3
# # 5 litre = 5/1000=0.005 m^
from scipy.sparse import csr_matrix
from scipy import constants
from scipy.optimize import root , minimize
import math
import numpy as np
from scipy.sparse.csc import csc_matrix
# #print(scipy.__version__)
# # constants

# volume = 5 # l

# print(f"5 l = {constants.liter * volume} m^3")

# print(f"pi = {constants.pi}")

# print(math.pi)

# # dir
# #print(dir(constants))

# print(int(constants.kilo * 500))

# # 1 byte = 1 octet
# # 1 byte has 8 bits 0 or 1
# # arrangement => 00 or 01 10 11


# print(7 * constants.kibi)

# print(constants.gram  * 5)

# # x + sin(x) non linear equations
# # numpy can solve or optimize a linear equation but non linear equation

# def equation1(x):
#     return x + math.cos(x)

# def equation2(x):
#     return math.pow(x,3)-1

# racines = root(equation1 , 0)
# racines2 = minimize(equation2 , 0 , method = 'BFGS')
# print(racines2)

data = np.array([
    [0, 0, 0], [0, 0, 1], [1, 0, 2]
])

data = csr_matrix(data)
print(data)
print("=" *20)
data.eliminate_zeros()
print(data)
print(csr_matrix(data).count_nonzero())
data.sum_duplicates()
print(data)

newdata = csc_matrix(data).tocsc()
print(newdata)

'''
1 1 2
1 0 1
0 0 1
'''

'''
1 1 2
1   1
    1
'''

