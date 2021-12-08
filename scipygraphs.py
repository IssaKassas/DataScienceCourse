# scipy using for data science
# machine learning using scipy , numpy , tensorflow
# pandas ,matplotlib

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

# arr = np.array([
#   [1, 1, 2],
#   [1, 3, 5],
#   [2, 5, 2]
# ])

# print(arr)
# arr2 = csr_matrix(arr)

# print(arr2)
# print(connected_components(arr2)
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
data = np.array([
    [1,2],
    [2,3],
    [5,0],
    [3,6],
    [4,4]
])

new= Delaunay(data).simplices

# plt.triplot()
plt.scatter(data[:,0] , data[:,1] , color = "#827349")
plt.triplot(data[:,0] , data[:,1] , new)
plt.show()
